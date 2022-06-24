from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/monturas/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos las monturas
@app.route('/monturas', methods=['GET'])
def listar_monturas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM montura ORDER BY id_montura;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        montura = []
        for fila in datos:
            data = {'id': fila[0], 'nombre': fila[1],
                    'descripcion': fila[2]}
            montura.append(data)
        return jsonify({'monturas': montura, 'mensaje': "Monturas listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un montura por id
def leer_monturas_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM montura WHERE id_montura  = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            monturas = {'id': datos[0],
                        'nombre': datos[1], 'descripcion': datos[2]}
            return monturas
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el montura por id desde end-point
@app.route('/monturas/<codigo>', methods=['GET'])
def leer_monturas(codigo):
    try:
        montura = leer_monturas_bd(codigo)
        if montura != None:
            return jsonify({'montura': montura, 'mensaje': "Montura encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Montura no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar montura en la base de datos via metodo POST HTTPS
@app.route('/monturas', methods=['POST'])
def registrar_montura():

    if (validar_montura(request.json['nombre'])):
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO montura (nombre, descripcion)
                VALUES ('{0}', '{1}')""".format(request.json['nombre'], request.json['descripcion'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Montura registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta para actualizar montura en la base de datos via metodo PUT HTTPS
@app.route('/monturas/<codigo>', methods=['PUT'])
def actualizar_monturas(codigo):
    if (validar_montura(request.json['nombre'])):
        try:
            usuarios = leer_monturas_bd(codigo)
            if usuarios != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE montura SET nombre = '{0}', descripcion = '{1}'
                WHERE id_montura = {2} """.format(request.json['nombre'], request.json['descripcion'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Montura actualizada.", 'exito': True})
            else:
                return jsonify({'mensaje': "Montura no encontrada.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/monturas/<codigo>', methods=['DELETE'])
def eliminar_monturas(codigo):
    try:
        usuarios = leer_monturas_bd(codigo)
        if usuarios != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM montura WHERE id_montura = {0} ".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Montura eliminada.", 'exito': True})
        else:
            return jsonify({'mensaje': "Montura no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
