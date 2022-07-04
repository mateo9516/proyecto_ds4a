from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
import psycopg2
from configparser import ConfigParser

app = Flask(__name__)



@app.route("/api/obtenerDf")

def obtenerDf():
    pqrs = []
    params = config()
    conexion = psycopg2.connect(**params)
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
    return jsonify(pqrs)


def config(archivo = 'Base_de_datos.ini', seccion = 'postgresql'):
    parser = ConfigParser()
    parser.read(archivo)


    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception ('seccion '+seccion+' no encontrada en el archivo '+archivo)
    
    return db


