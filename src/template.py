from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/????/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los ????
# @app.route('/????', methods=['GET'])
# def listar_usuarios():
#     try:
#         cursor = conexion.connection.cursor()
#         sql = "SELECT usuarios.id_usuario, usuarios.nombre, usuarios.paswd, roles.rol, estado.estado FROM usuarios JOIN roles ON usuarios.rol = roles.id_rol JOIN estado ON usuarios.id_estado = estado.id_estado ORDER BY usuarios.id_usuario;"
#         cursor.execute(sql)
#         datos = cursor.fetchall()
#         usuarios = []
#         for fila in datos:
#             data = {'id': fila[0], 'nombre': fila[1],
#                     'contrasenia': fila[2], 'rol': fila[3], 'estado': fila[4]}
#             usuarios.append(data)
#         return jsonify({'usuarios': usuarios, 'mensaje': "usuarios listados.", 'exito': True})
#     except Exception as ex:
#         return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un ???? por id
# def leer_usuarios_bd(codigo):
#     try:
#         cursor = conexion.connection.cursor()
#         sql = "SELECT usuarios.id_usuario, usuarios.nombre, usuarios.paswd, roles.rol, estado.estado FROM usuarios JOIN roles ON usuarios.rol = roles.id_rol JOIN estado ON usuarios.id_estado = estado.id_estado WHERE usuarios.id_usuario = '{0}'".format(
#             codigo)
#         cursor.execute(sql)
#         datos = cursor.fetchone()
#         if datos != None:
#             usuarios = {'id': datos[0],
#                         'nombre': datos[1], 'contrasenia': datos[2], 'rol': datos[3], 'estado': datos[4]}
#             return usuarios
#         else:
#             return None
#     except Exception as ex:
#         raise ex


# ruta para listar el ???? por id desde end-point
# @app.route('/????/<codigo>', methods=['GET'])
# def leer_usuario(codigo):
#     try:
#         usuario = leer_usuarios_bd(codigo)
#         if usuario != None:
#             return jsonify({'usuario': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
#         else:
#             return jsonify({'mensaje': "usuario no encontrado.", 'exito': False})
#     except Exception as ex:
#         return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar ???? en la base de datos via metodo POST HTTPS
# @app.route('/????', methods=['POST'])
# def registrar_usuario():

#     if (validar_nombre_usuario(request.json['nombre'])):
#         try:
#             cursor = conexion.connection.cursor()
#             sql = """INSERT INTO usuarios (nombre, paswd, rol, id_estado)
#                 VALUES ('{0}', '{1}', {2}, {3})""".format(request.json['nombre'], request.json['pass'], request.json['rol'], request.json['estado'])
#             cursor.execute(sql)
#             # Confirma la acci??n de inserci??n.
#             conexion.connection.commit()
#             return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
#         except Exception as ex:
#             return jsonify({'mensaje': "Error", 'exito': False})
#     else:
#         return jsonify({'mensaje': "Par??metros inv??lidos...", 'exito': False})


# ruta para actualizar ???? en la base de datos via metodo PUT HTTPS
# @app.route('/????/<codigo>', methods=['PUT'])
# def actualizar_usuarios(codigo):
#     if (validar_nombre_usuario(request.json['nombre'])):
#         try:
#             usuarios = leer_usuarios_bd(codigo)
#             if usuarios != None:
#                 cursor = conexion.connection.cursor()
#                 sql = """UPDATE usuarios SET nombre = '{0}', paswd = '{1}', rol = {2}, id_estado = {3}
#                 WHERE id_usuario = {4} """.format(request.json['nombre'], request.json['pass'], request.json['rol'], request.json['estado'], codigo)
#                 cursor.execute(sql)
#                 # Confirma la acci??n de actualizaci??n.
#                 conexion.connection.commit()
#                 return jsonify({'mensaje': "Usuario actualizado.", 'exito': True})
#             else:
#                 return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
#         except Exception as ex:
#             return jsonify({'mensaje': "Error", 'exito': False})
#     else:
#         return jsonify({'mensaje': "Par??metros inv??lidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
# @app.route('/????/<codigo>', methods=['DELETE'])
# def eliminar_usuarios(codigo):
#     try:
#         usuarios = leer_usuarios_bd(codigo)
#         if usuarios != None:
#             cursor = conexion.connection.cursor()
#             sql = "DELETE FROM usuarios WHERE id_usuario = {0} ".format(codigo)
#             cursor.execute(sql)
#             conexion.connection.commit()  # Confirma la acci??n de eliminaci??n.
#             return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
#         else:
#             return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
#     except Exception as ex:
#         return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ??? </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
