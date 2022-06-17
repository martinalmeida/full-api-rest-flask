from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

CORS(app, resources={r"/cursos/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT usuarios.id_usuario, usuarios.nombre, usuarios.paswd, roles.rol, estado.estado FROM usuarios JOIN roles ON usuarios.rol = roles.id_rol JOIN estado ON usuarios.id_estado = estado.id_estado ORDER BY usuarios.id_usuario;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            curso = {'id': fila[0], 'nombre': fila[1],
                     'contrasenia': fila[2], 'rol': fila[3], 'estado': fila[4]}
            usuarios.append(curso)
        return jsonify({'usuarios': usuarios, 'mensaje': "usuarios listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un usuario por id
def leer_usuarios_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT usuarios.id_usuario, usuarios.nombre, usuarios.paswd, roles.rol, estado.estado FROM usuarios JOIN roles ON usuarios.rol = roles.id_rol JOIN estado ON usuarios.id_estado = estado.id_estado WHERE usuarios.id_usuario = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuarios = {'id': datos[0],
                        'nombre': datos[1], 'contrasenia': datos[2], 'rol': datos[3], 'estado': datos[4]}
            return usuarios
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el usuario por id desde end-point
@app.route('/usuarios/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        usuario = leer_usuarios_bd(codigo)
        if usuario != None:
            return jsonify({'usuario': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar usuario en la base de datos via metodo POST HTTPS
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():

    if (validar_codigo(request.json['codigo']) and validar_nombre(request.json['nombre'])):
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO usuarios (codigo, nombre, creditos) 
                VALUES ('{0}', '{1}', {2})""".format(request.json['codigo'],
                                                     request.json['nombre'], request.json['creditos'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    if (validar_codigo(codigo) and validar_nombre(request.json['nombre'])):
        try:
            curso = leer_usuarios_bd(codigo)
            if curso != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE curso SET nombre = '{0}', creditos = {1} 
                WHERE codigo = '{2}'""".format(request.json['nombre'], request.json['creditos'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Curso actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        curso = leer_usuarios_bd(codigo)
        if curso != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Curso eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
