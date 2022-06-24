from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/sintomas/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los sintomas
@app.route('/sintomas', methods=['GET'])
def listar_sintomas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM sintomas ORDER BY id_sintoma;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        sintomas = []
        for fila in datos:
            curso = {'id': fila[0], 'nombre': fila[1],
                     'descripcion': fila[2]}
            sintomas.append(curso)
        return jsonify({'sintomas': sintomas, 'mensaje': "sintomas listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un sintomas por id
def leer_sintomas_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM sintomas WHERE id_sintoma = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            sintomas = {'id': datos[0],
                        'nombre': datos[1], 'descripcion': datos[2]}
            return sintomas
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el sintoma por id desde end-point
@app.route('/sintomas/<codigo>', methods=['GET'])
def leer_sintoma(codigo):
    try:
        sintoma = leer_sintomas_bd(codigo)
        if sintoma != None:
            return jsonify({'sintoma': sintoma, 'mensaje': "sintoma encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "sintoma no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar sintoma en la base de datos via metodo POST HTTPS
@app.route('/sintomas', methods=['POST'])
def registrar_sintoma():

    if (validar_sintoma(request.json['nombre'])):
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO sintomas (nombre, descripcion)
                VALUES ('{0}', '{1}')""".format(request.json['nombre'], request.json['descripcion'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Sintoma registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta para actualizar sintoma en la base de datos via metodo PUT HTTPS
@app.route('/sintomas/<codigo>', methods=['PUT'])
def actualizar_sintoma(codigo):
    if (validar_sintoma(request.json['nombre'])):
        try:
            sintomas = leer_sintomas_bd(codigo)
            if sintomas != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE sintomas SET nombre = '{0}', descripcion = '{1}'
                WHERE id_sintoma = {2} """.format(request.json['nombre'], request.json['descripcion'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Sintoma actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Sintoma no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/sintomas/<codigo>', methods=['DELETE'])
def eliminar_sintoma(codigo):
    try:
        sintoma = leer_sintomas_bd(codigo)
        if sintoma != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM sintomas WHERE id_sintoma = {0} ".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Sintoma eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Sintoma no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
