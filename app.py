from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
import json, csv, os

from Logica import carga_descarga


app = Flask(__name__)


@app.route("/api/obtenerDf")

def obtenerDf():
    respuesta = carga_descarga.descargaDatos()
    return jsonify(respuesta)

@app.route("/api/consultaid/<id>/")

def consultaid(id):
    respuesta = carga_descarga.consulta(id)
    return jsonify(respuesta)

@app.route("/api/add/", methods= ["POST"])

def cargaDatos():
    
    estructura= request.get_json()

    respuesta = carga_descarga.cargaDatos(estructura)
    if respuesta == 1:
        return "Exito"
    else:
        return jsonify({"message": "Error on insert"}), 500


@app.route("/api/cargaMasiva", methods=["POST"])

def cargaMasiva():
    csvF = 'data/pqr_radicacions.csv'
    jsonf = 'data/pqr_radicacions.json'
    
    estructuras = csv2Json(csvF,jsonf)
    
    salida = 0

    for estructura in estructuras:
        carga_descarga.cargaDatos(estructuras[estructura])
        salida += 1
        print(salida)
    
    if salida == len(estructuras):
        os.remove('data/pqr_radicacions.json')
        csvF = 'data/pqr_radicacions.csv'
        return "cargado con exito"
    else:
         return jsonify({"message": "Error en la carga"}), 500


def csv2Json(a,b):
    csvFilePath = a
    JSONFilePath = b

    data = {}

    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=';')
        for rows in csvReader:
            id = rows['id']
            data[id] = rows

    with open(JSONFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))
        return data