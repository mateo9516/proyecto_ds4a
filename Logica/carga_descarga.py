from ast import Raise
from configparser import ConfigParser
import psycopg2
import csv
import Logica.transformadores as transformadores
import Logica.modelos as modelos


conexion = psycopg2.connect(
    host= 'localhost', #'ec2-18-204-142-254.compute-1.amazonaws.com',
    user=  'postgres',#'qfkvlglgixbnqp',
    password= '1234',#"5ddacab9748c3174f125b342bef9a2363a6cce60ac79c286a872d1c5f1108744",
    database= 'new' #"dd0ibbfpq96r39"
)

def cargaDatos(estructura):
    entidad = estructura["glb_entidad_id"]
    derechos = estructura["pqr_tipo_derechos_id"]
    solicitudEsp = estructura["otros_tipo_solicitud_esp"]
    solicitud = estructura["pqr_tipo_solicitud_id"]
    asunto =  estructura["asunto"]
    tipoCaracterizacion  = "Automatica"


    if entidad == '':
        entidad = modelos.procesoEntidad(asunto)
        
    if derechos == '':
        derechos = modelos.procesoDerecho(asunto)
        
    if solicitudEsp == '':
        solicitudEsp = modelos.procesoSoliEsp(asunto)
        
    if solicitud == '':
        solicitud = modelos.procesoSoli(asunto)




    try:
        with conexion.cursor() as cursor:
            sql="""INSERT INTO pqr_radicacions (glb_estado_id, glb_dependencia_id, pqr_derechos_id, ase_tipo_poblacion_id, 
                            ase_tipo_regimen_id, pqr_tipo_solicitud_id, pqr_tipo_solicitud_especifica_id, glb_barrio_vereda_id, 
                            glb_tipo_identificacion_id, identificacion, primer_apellido, segundo_apellido, primer_nombre, segundo_nombre, 
                            direccion, telefono_fijo, telefono_movil, email, ficha_sisben, clasificacion_sisben, no_radicacion, fecha_radicacion, 
                            fecha_vencimiento , no_respuesta, asunto, otros_tipo_solicitud_esp, amisalud_id, nombre_completo, fecha_nacimiento, 
                            latitud, longitud, estado_respuesta, estado_tiempo, glb_tipo_genero_id, glb_entidad_id, barrio, vereda, suelo, comuna, 
                            fecha_respuesta, tipo_caracterizacion) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,
                             %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
            
            for x in estructura:
                if estructura[x]=='':
                    estructura[x]=None

            if None not in [estructura.get('glb_entidad_id'),estructura.get('pqr_tipo_derechos_id'),estructura.get('otros_tipo_solicitud_esp'),estructura.get('pqr_tipo_solicitud_id')]:
                tipoCaracterizacion = 'Manual'

            cursor.execute(sql,(estructura.get("glb_estado_id"), estructura.get("glb_dependencia_id"), derechos, 
                                estructura.get("ase_tipo_poblacion_id"), estructura.get("ase_tipo_regimen_id"), solicitud,
                                solicitudEsp, estructura.get("glb_barrio_vereda_id"),
                                estructura.get("glb_tipo_identificacion_id"), estructura.get("identificacion"),estructura.get("primer_apellido"), 
                                estructura.get("segundo_apellido"), estructura.get("primer_nombre"), estructura.get("segundo_nombre"), estructura.get("direccion"),
                                estructura.get("telefono_fijo"), estructura.get("telefono_movil"), estructura.get("email"), estructura.get("ficha_sisben"), 
                                estructura.get("clasificacion_sisben"),estructura.get("no_radicacion"), estructura.get("fecha_radicacion"), estructura.get("fecha_vencimiento"),
                                estructura.get("no_respuesta"), estructura.get("asunto"),estructura.get("otros_tipo_solicitud_esp"), estructura.get("amisalud_id"), 
                                estructura.get("nombre_completo"), estructura.get("fecha_nacimiento"), estructura.get("Latitud"),estructura.get("Longitud"), 
                                transformadores.estado_respuesta(estructura.get("glb_estado_id")), transformadores.estado_tiempo(estructura.get("fecha_vencimiento"),
                                estructura.get("fecha_respuesta")),estructura.get("glb_tipo_genero_id"), entidad, 
                                estructura.get("Barrio"), estructura.get("Vereda"), estructura.get("Suelo"), estructura.get("Comuna"), estructura.get("fecha_respuesta"), tipoCaracterizacion))
            affected_rows= cursor.rowcount
            conexion.commit()
        return affected_rows            
    except Exception as ex:
        raise Exception(ex)

def descargaDatos():
    pqrs = []
    cur = conexion.cursor()
    exito = 0
    cur.execute('SELECT * FROM pqr_radicacions;')
    pqrs_raw = cur.fetchall()
    for pqr in pqrs_raw:
        if exito == 0:
            print(pqr[0],pqr[1])
            exito = 1
        result = {
            'id': pqr[0], 
            'glb_estado_id':pqr[1], 
            'glb_dependencia_id':pqr[2], 
            'pqr_tipo_derechos_id':pqr[3], 
            'ase_tipo_poblacion_id':pqr[4], 
            'ase_tipo_regimen_id':pqr[5],
            'pqr_tipo_solicitud_id':pqr[6], 
            'global_barrio_vereda_id':pqr[7],
            'glb_tipo_identificacion_id':pqr[8],
            'identificacion':pqr[9], 
            'primer_apellido':pqr[10], 
            'segundo_apellido':pqr[11], 
            'primer_nombre':pqr[12], 
            'segundo_nombre':pqr[13], 
            'direccion':pqr[14],
            'telefono_fijo':pqr[15],
            'email':pqr[16],  
            'ficha_sisben':pqr[17], 
            'clasificacion_sisben':pqr[18],
            'no_radicacion':pqr[19], 
            'fecha_radicacion':pqr[20],
            'fecha_vencimiento':pqr[21],
            'no_respuesta':pqr[22],
            'asunto':pqr[23],
            'otros_tipo_solicitud_esp':pqr[24],
            'amisalud_id':pqr[25],
            'nombre_completo':pqr[26],
            'fecha_nacimiento':pqr[27],
            'Latitud': pqr[28],
            'Longitud': pqr[29],
            'estado_respuesta':pqr[30],
            'estado_tiempo':pqr[31],
            'glb_tipo_genero_id':pqr[32],
            'glb_entidad_id':pqr[33],
            'barrio':pqr[34],
            'vereda':pqr[35],
            'suelo':pqr[36],
            'comuna':pqr[37],
            'fecha_respuesta':pqr[38],
            'tipo_caracterizacion':pqr[39],
            'telefono_movil':pqr[40],
            'pqr_tipo_solicitud_especifica_id':pqr[41]
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


def correr_frase(frase):
    entidad = modelos.procesoEntidad(frase.get('frase'))
    derechos = modelos.procesoDerecho(frase.get('frase'))
    solicitudEsp = modelos.procesoSoliEsp(frase.get('frase'))
    solicitud = modelos.procesoSoli(frase.get('frase'))
    
    return {"entidad":entidad,
            "derechos":derechos,
            "solicitudEsp":solicitudEsp,
            "solicitud": solicitud
            }