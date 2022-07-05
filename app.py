from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

from Logica import carga_descarga


app = Flask(__name__)



@app.route("/api/obtenerDf")

def obtenerDf():
    respuesta = carga_descarga.descargaDatos()
    return jsonify(respuesta)