from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/facturas/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los facturas
@app.route('/facturas', methods=['GET'])
def listar_facturas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT facturas.id_factura, facturas.fecha_creacion, facturas.array_productos, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM facturas JOIN paciente ON facturas.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON facturas.id_usuario = usuarios.id_usuario JOIN estado ON facturas.id_estado = estado.id_estado ORDER BY facturas.id_factura;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        facturas = []
        for fila in datos:
            data = {'id': fila[0], 'fecha_creacion': fila[1],
                    'array_productos': fila[2], 'tp_doc': fila[3], 'documento': fila[4], 'paciente': fila[5], 'usuario': fila[6], 'estado ': fila[7]}
            facturas.append(data)
        return jsonify({'facturas': facturas, 'mensaje': "facturas listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un facturas por id
def leer_facturas_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT facturas.id_factura, facturas.fecha_creacion, facturas.array_productos, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM facturas JOIN paciente ON facturas.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON facturas.id_usuario = usuarios.id_usuario JOIN estado ON facturas.id_estado = estado.id_estado WHERE facturas.id_factura = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            facturas = {'id': datos[0], 'fecha_creacion': datos[1],
                        'array_productos': datos[2], 'tp_doc': datos[3], 'documento': datos[4], 'paciente': datos[5], 'usuario': datos[6], 'estado ': datos[7]}
            return facturas
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el facturas por id desde end-point
@app.route('/facturas/<codigo>', methods=['GET'])
def leer_factura(codigo):
    try:
        factura = leer_facturas_bd(codigo)
        if factura != None:
            return jsonify({'factura': factura, 'mensaje': "factura encontrada.", 'exito': True})
        else:
            return jsonify({'mensaje': "factura no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar facturas en la base de datos via metodo POST HTTPS
@app.route('/facturas', methods=['POST'])
def registrar_factura():
    try:
        fecha_actual = datetime.today()
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO facturas (fecha_creacion, array_productos, id_paciente, id_usuario, id_estado)
            VALUES ('{0}', '{1}', {2}, {3}, {4})""".format(fecha_actual, request.json['productos'], request.json['paciente'], request.json['usuario'], request.json['estado'])
        cursor.execute(sql)
        # Confirma la acción de inserción.
        conexion.connection.commit()
        return jsonify({'mensaje': "Factura registrado.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para actualizar facturas en la base de datos via metodo PUT HTTPS
@app.route('/facturas/<codigo>', methods=['PUT'])
def actualizar_facturas(codigo):
    try:
        fecha_actual = datetime.today()
        facturas = leer_facturas_bd(codigo)
        if facturas != None:
            cursor = conexion.connection.cursor()
            sql = """UPDATE facturas SET fecha_creacion = '{0}', array_productos = '{1}', id_paciente = {2}, id_usuario = {3}, id_estado = {4}
            WHERE id_factura = {5} """.format(fecha_actual, request.json['productos'], request.json['paciente'], request.json['usuario'], request.json['estado'], codigo)
            cursor.execute(sql)
            # Confirma la acción de actualización.
            conexion.connection.commit()
            return jsonify({'mensaje': "Factura actualizada.", 'exito': True})
        else:
            return jsonify({'mensaje': "Factura no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/facturas/<codigo>', methods=['DELETE'])
def eliminar_factura(codigo):
    try:
        usuarios = leer_facturas_bd(codigo)
        if usuarios != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM facturas WHERE id_factura = {0} ".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "factura eliminada.", 'exito': True})
        else:
            return jsonify({'mensaje': "factura no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
