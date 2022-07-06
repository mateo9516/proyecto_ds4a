from ast import Raise
from configparser import ConfigParser
import psycopg2
import csv
import Logica.transformadores as transformadores


conexion = psycopg2.connect(
    host= 'ec2-18-204-142-254.compute-1.amazonaws.com',
    user= 'qfkvlglgixbnqp',
    password= "5ddacab9748c3174f125b342bef9a2363a6cce60ac79c286a872d1c5f1108744",
    database= "dd0ibbfpq96r39"
)

def cargaDatos(estructura):
    try:    
        with conexion.cursor() as cursor:
            sql="""INSERT INTO pqr_radicacions (glb_estado_id, glb_dependencia_id, pqr_derechos_id, ase_tipo_poblacion_id, 
                            ase_tipo_regimen_id, pqr_tipo_solicitud_id, pqr_tipo_solicitud_especifica_id, glb_barrio_vereda_id, 
                            glb_tipo_identificacion_id, identificacion, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, 
                            direccion, telefono_fijo, telefono_movil, email, ficha_sisben, clasificacion_sisben, no_radicacion, fecha_radicacion, 
                            fecha_vencimiento , no_respuesta, asunto, otros_tipo_solicitud_esp, amisalud_id, nombre_completo, fecha_nacimiento, 
                            latitud, longitud, estado_respuesta, estado_tiempo, glb_tipo_genero_id, glb_entidad_id, barrio, vereda, suelo, comuna, fecha_respuesta) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for x in estructura:
                if estructura[x]=='':
                    estructura[x]=None

            cursor.execute(sql,(estructura.get("glb_estado_id"), estructura.get("glb_dependencia_id"), 
                             estructura.get("pqr_tipo_derechos_id"), estructura.get("ase_tipo_poblacion_id"), estructura.get("ase_tipo_regimen_id"), 
                             estructura.get("pqr_tipo_solicitud_id"),estructura.get("pqr_tipo_solicitud_especifica_id"), estructura.get("glb_barrio_vereda_id"),
                             estructura.get("glb_tipo_identificacion_id"), estructura.get("identificacion"),estructura.get("primer_apellido"), 
                             estructura.get("segundo_apellido"), estructura.get("primer_nombre"), estructura.get("segundo_nombre"), estructura.get("direccion"),
                             estructura.get("telefono_fijo"), estructura.get("telefono_movil"), estructura.get("email"), estructura.get("ficha_sisben"), 
                             estructura.get("clasificacion_sisben"),estructura.get("no_radicacion"), estructura.get("fecha_radicacion"), estructura.get("fecha_vencimiento"),
                             estructura.get("no_respuesta"), estructura.get("asunto"),estructura.get("otros_tipo_solicitud_esp"), estructura.get("amisalud_id"), 
                             estructura.get("nombre_completo"), estructura.get("fecha_nacimiento"), estructura.get("latitud"),estructura.get("longitud"), 
                             transformadores.estado_respuesta(estructura.get("glb_estado_id")), transformadores.estado_tiempo(estructura.get("fecha_vencimiento"),estructura.get("fecha_respuesta")), estructura.get("glb_tipo_genero_id"), estructura.get("glb_entidad_id"), 
                             estructura.get("barrio"), estructura.get("vereda"), estructura.get("suelo"), estructura.get("comuna"), estructura.get("fecha_respuesta")))
            affected_rows= cursor.rowcount
            conexion.commit()
        return affected_rows            
    except Exception as ex:
        raise Exception(ex)

def descargaDatos():
    pqrs = []
    cur = conexion.cursor()
    cur.execute('SELECT * FROM pqr_radicacions;')
    pqrs_raw = cur.fetchall()
    for pqr in pqrs_raw:
        result = {
            'id': pqr[0], 
            'glb_estado_id':pqr[1], 
            'glb_dependencia_id':pqr[2], 
            'pqr_tipo_derechos_id':pqr[3], 
            'ase_tipo_poblacion_id':pqr[4], 
            'ase_tipo_regimen_id':pqr[5],
            'pqr_tipo_solicitud_id':pqr[6], 
            'pqr_tipo_solicitud_especifica_id':pqr[7],
            'glb_barrio_vereda_id':pqr[8],
            'gbl_tipo_identificacion_id':pqr[9], 
            'identificacion':pqr[10], 
            'primer_apellido':pqr[11], 
            'segundo_apellido':pqr[12],
            'primer_nombre':pqr[13], 
            'segundo_nombre':pqr[14], 
            'direccion':pqr[15],
            'telefono_fijo':pqr[16],
            'telefono_movil':pqr[17], 
            'email':pqr[18], 
            'ficha_sisben':pqr[19], 
            'clasificacion_sisben':pqr[20],
            'no_radicacion':pqr[21], 
            'fecha_radicacion':pqr[22],
            'fecha_vencimiento':pqr[23],
            'no_respuesta':pqr[24],
            'asunto':pqr[25],
            'otros_tipo_solicitud_esp':pqr[26],
            'amisalud_id':pqr[27],
            'nombre_completo':pqr[28],
            'fecha_nacimiento':pqr[29],
            'fecha_respuesta':pqr[30],
            'Latitud': pqr[31],
            'Longitud': pqr[32],
            'estado_respuesta':pqr[33],
            'estado_tiempo':pqr[34],
            'glb_tipo_genero_id':pqr[35],
            'glb_entidad_id':pqr[36],
            'barrio':pqr[37],
            'vereda':pqr[38],
            'suelo':pqr[39],
            'comuna':pqr[40],

        }
        pqrs.append(result)
    return pqrs

def consulta(id):
    try:         
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM pqr_radicacions WHERE primer_nombre = %s", (id,))
            pqr = cursor.fetchone()

            pqrs = None
            if pqr != None:
                pqrs = {
                    'id': pqr[0], 
                    'glb_estado_id':pqr[1], 
                    'glb_dependencia_id':pqr[2], 
                    'pqr_tipo_derechos_id':pqr[3], 
                    'ase_tipo_poblacion_id':pqr[4], 
                    'ase_tipo_regimen_id':pqr[5],
                    'pqr_tipo_solicitud_id':pqr[6], 
                    'pqr_tipo_solicitud_especifica_id':pqr[7],
                    'glb_barrio_vereda_id':pqr[8],
                    'gbl_tipo_identificacion_id':pqr[9], 
                    'identificacion':pqr[10], 
                    'primer_apellido':pqr[11], 
                    'segundo_apellido':pqr[12],
                    'primer_nombre':pqr[13], 
                    'segundo_nombre':pqr[14], 
                    'direccion':pqr[15],
                    'telefono_fijo':pqr[16],
                    'telefono_movil':pqr[17], 
                    'email':pqr[18], 
                    'ficha_sisben':pqr[19], 
                    'clasificacion_sisben':pqr[20],
                    'no_radicacion':pqr[21], 
                    'fecha_radicacion':pqr[22],
                    'fecha_vencimiento':pqr[23],
                    'no_respuesta':pqr[24],
                    'asunto':pqr[25],
                    'otros_tipo_solicitud_esp':pqr[26],
                    'amisalud_id':pqr[27],
                    'nombre_completo':pqr[28],
                    'fecha_nacimiento':pqr[29],
                    'fecha_respuesta':pqr[30],
                    'Latitud': pqr[31],
                    'Longitud': pqr[32],
                    'estado_respuesta':pqr[33],
                    'estado_tiempo':pqr[34],
                    'glb_tipo_genero_id':pqr[35],
                    'glb_entidad_id':pqr[36],
                    'barrio':pqr[37],
                    'vereda':pqr[38],
                    'suelo':pqr[39],
                    'comuna':pqr[40],
                    }
        return pqrs     
    except Exception as ex:
        raise Exception(ex)
