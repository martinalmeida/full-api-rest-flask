from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/login/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# consulta para listar un usuario por nombre y contraseña
def leer_usuarios_bd(nombre, passwd):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM usuarios WHERE nombre = '{0}' AND paswd = '{1}' ".format(
            nombre, passwd)
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


# ruta para listar el usuario por nombre y contraseña desde end-point
@app.route('/login/<nombre>/<passwd>', methods=['GET'])
def leer_usuario(nombre, passwd):
    try:
        usuario = leer_usuarios_bd(nombre, passwd)
        if usuario != None:
            return jsonify({'usuario': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
