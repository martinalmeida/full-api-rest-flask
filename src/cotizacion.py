from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/cotizacion/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todas los cotizaciones
@app.route('/cotizacion', methods=['GET'])
def listar_cotizacion():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT cotizacion.id_cotizacion, cotizacion.fecha, (lente.nombre)lente, (montura.nombre)montura, cotizacion.valor, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario FROM cotizacion JOIN lente ON cotizacion.id_cotizacion = lente.id JOIN montura ON cotizacion.id_montura = montura.id_montura JOIN paciente ON cotizacion.id_paciente = paciente.id_paciente JOIN usuarios ON cotizacion.id_usuario = usuarios.id_usuario ORDER BY cotizacion.id_cotizacion;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cotizacion = []
        for fila in datos:
            data = {'id': fila[0], 'fecha': fila[1],
                    'lente': fila[2], 'montura': fila[3], 'valor': fila[4], 'documento': fila[5], 'paciente': fila[6], 'usuario': fila[7]}
            cotizacion.append(data)
        return jsonify({'cotizaciones': cotizacion, 'mensaje': "cotizaciones listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un cotizacion por id
def leer_cotizacion_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT cotizacion.id_cotizacion, cotizacion.fecha, (lente.nombre)lente, (montura.nombre)montura, cotizacion.valor, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario FROM cotizacion JOIN lente ON cotizacion.id_cotizacion = lente.id JOIN montura ON cotizacion.id_montura = montura.id_montura JOIN paciente ON cotizacion.id_paciente = paciente.id_paciente JOIN usuarios ON cotizacion.id_usuario = usuarios.id_usuario WHERE cotizacion.id_cotizacion = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            cotizaciones = {'id': datos[0],
                            'fecha': datos[1], 'lente': datos[2], 'montura': datos[3], 'valor': datos[4], 'documento': datos[5], 'paciente': datos[6], 'usuario': datos[7]}
            return cotizaciones
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el cotizacion por id desde end-point
@app.route('/cotizacion/<codigo>', methods=['GET'])
def leer_cotizacion(codigo):
    try:
        cotizacion = leer_cotizacion_bd(codigo)
        if cotizacion != None:
            return jsonify({'cotizacion': cotizacion, 'mensaje': "cotizacion encontrada.", 'exito': True})
        else:
            return jsonify({'mensaje': "cotizacion no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar cotizacion en la base de datos via metodo POST HTTPS
@app.route('/cotizacion', methods=['POST'])
def registrar_cotizacion():

    if (validar_fecha(request.json['fecha']) and validar_valor(request.json['valor'])):
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO cotizacion (fecha, id_lente, id_montura, valor, id_paciente, id_usuario)
                VALUES ('{0}', {1}, {2}, '{3}', {4}, {5})""".format(request.json['fecha'], request.json['lente'], request.json['montura'], request.json['valor'], request.json['paciente'], request.json['usuario'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Cotizacion registrada.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta para actualizar cotizacion en la base de datos via metodo PUT HTTPS
@app.route('/cotizacion/<codigo>', methods=['PUT'])
def actualizar_cotizacion(codigo):
    if (validar_fecha(request.json['fecha']) and validar_valor(request.json['valor'])):
        try:
            cotizacion = leer_cotizacion_bd(codigo)
            if cotizacion != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE cotizacion SET fecha = '{0}', id_lente = {1}, id_montura = {2}, valor = '{3}', id_paciente = {4}, id_usuario = {5}
                WHERE id_cotizacion = {6} """.format(request.json['fecha'], request.json['lente'], request.json['montura'], request.json['valor'], request.json['paciente'], request.json['usuario'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Cotizacion actualizada.", 'exito': True})
            else:
                return jsonify({'mensaje': "Cotizacion no encontrada.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/cotizacion/<codigo>', methods=['DELETE'])
def eliminar_cotizacion(codigo):
    try:
        cotizacion = leer_cotizacion_bd(codigo)
        if cotizacion != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM cotizacion WHERE id_cotizacion = {0} ".format(
                codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Cotizacion eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Cotizacion no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
