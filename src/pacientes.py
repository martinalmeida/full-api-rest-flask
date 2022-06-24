from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/pacientes/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los pacientes
@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT paciente.id_paciente, paciente.nombres, paciente.apellidos, (tipo_documento.nombre)nomdoc, paciente.documento, paciente.fecha_nacimiento, paciente.celular, paciente.whatsapp, usuarios.nombre, estado.estado FROM paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON paciente.id_usuario = usuarios.id_usuario JOIN estado ON paciente.id_estado = estado.id_estado ORDER BY paciente.id_paciente;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        pacientes = []
        for fila in datos:
            data = {'id': fila[0],
                    'nombres': fila[1], 'apellidos': fila[2], 'tipoDocumento': fila[3], 'documento': fila[4], 'fechaNacimiento': fila[5], 'celular': fila[6], 'whatsapp': fila[7], 'usuario': fila[8], 'estado': fila[9]}
            pacientes.append(data)
        return jsonify({'pacientes': pacientes, 'mensaje': "pacientes listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un pacientes por id
def leer_pacientes_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT paciente.id_paciente, paciente.nombres, paciente.apellidos, (tipo_documento.nombre)nomdoc, paciente.documento, paciente.fecha_nacimiento, paciente.celular, paciente.whatsapp, usuarios.nombre, estado.estado FROM paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON paciente.id_usuario = usuarios.id_usuario JOIN estado ON paciente.id_estado = estado.id_estado WHERE paciente.id_paciente = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            pacientes = {'id': datos[0],
                         'nombres': datos[1], 'apellidos': datos[2], 'tipoDocumento': datos[3], 'documento': datos[4], 'fechaNacimiento': datos[5], 'celular': datos[6], 'whatsapp': datos[7], 'usuario': datos[8], 'estado': datos[9]}
            return pacientes
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el pacientes por id desde end-point
@app.route('/pacientes/<codigo>', methods=['GET'])
def leer_paciente(codigo):
    try:
        paciente = leer_pacientes_bd(codigo)
        if paciente != None:
            return jsonify({'paciente': paciente, 'mensaje': "paciente encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "paciente no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar paciente en la base de datos via metodo POST HTTPS
@app.route('/pacientes', methods=['POST'])
def registrar_pacientes():

    if (validar_nombre_paciente(request.json['nombres']) and validar_celular(request.json['celular']) and validar_celular(request.json['whatsapp'])):
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO paciente (nombres, apellidos, id_documento, documento, fecha_nacimiento, celular, whatsapp, id_usuario, id_estado) 
                VALUES ('{0}', '{1}', {2}, '{3}', '{4}', '{5}', '{6}', {7}, {8})""".format(request.json['nombres'], request.json['apellidos'], request.json['tpDoc'], request.json['documento'], request.json['fecha'], request.json['celular'], request.json['whatsapp'], request.json['usuario'], request.json['estado'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Paciente registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta para actualizar paciente en la base de datos via metodo PUT HTTPS
@app.route('/pacientes/<codigo>', methods=['PUT'])
def actualizar_pacientes(codigo):
    if (validar_nombre_paciente(request.json['nombres']) and validar_celular(request.json['celular']) and validar_celular(request.json['whatsapp'])):
        try:
            pacientes = leer_pacientes_bd(codigo)
            if pacientes != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE paciente SET nombres = '{0}', apellidos = '{1}', id_documento = {2}, documento = '{3}', fecha_nacimiento = '{4}', celular = '{5}', whatsapp = '{6}', id_usuario = {7}, id_estado = {8}
                WHERE id_paciente = {9} """.format(request.json['nombres'], request.json['apellidos'], request.json['tpDoc'], request.json['documento'], request.json['fecha'], request.json['celular'], request.json['whatsapp'], request.json['usuario'], request.json['estado'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Paciente actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Paciente no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/pacientes/<codigo>', methods=['DELETE'])
def eliminar_usuarios(codigo):
    try:
        pacientes = leer_pacientes_bd(codigo)
        if pacientes != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM paciente WHERE id_paciente = {0} ".format(
                codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Paciente eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Paciente no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
