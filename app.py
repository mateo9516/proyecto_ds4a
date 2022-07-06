from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

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
    estructuras = request.get_json()
    salida = 0

    for estructura in estructuras:
        print(estructuras[estructura])
        carga_descarga.cargaDatos(estructuras[estructura])
        salida += 1
    
    if salida == len(estructuras):
        return "cargado con exito"
    else:
         return jsonify({"message": "Error en la carga"}), 500