from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/formulas/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los formulas
@app.route('/formulas', methods=['GET'])
def listar_formulas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT formulas.id_formula, formulas.proximo_control, formulas.vigencia, formulas.distancia_pupilar, (lente.nombre)lente, (filtro.nombre)filtro, formulas.observacion, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM formulas JOIN lente ON formulas.id_lente = lente.id JOIN filtro ON formulas.id_filtro = filtro.id JOIN paciente ON formulas.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON formulas.id_usuario = usuarios.id_usuario JOIN estado ON formulas.id_estado = estado.id_estado ORDER BY formulas.id_formula;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        formulas = []
        for fila in datos:
            data = {'id': fila[0], 'control': fila[1],
                    'vigencia': fila[2], 'distancia': fila[3], 'lente': fila[4], 'filtro': fila[5], 'observacion': fila[6], 'tp_doc': fila[7], 'documento': fila[8], 'paciente': fila[9], 'usuario': fila[10], 'estado': fila[11]}
            formulas.append(data)
        return jsonify({'formulas': formulas, 'mensaje': "formulas listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un formulas por id
def leer_formulas_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT formulas.id_formula, formulas.proximo_control, formulas.vigencia, formulas.distancia_pupilar, (lente.nombre)lente, (filtro.nombre)filtro, formulas.observacion, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM formulas JOIN lente ON formulas.id_lente = lente.id JOIN filtro ON formulas.id_filtro = filtro.id JOIN paciente ON formulas.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON formulas.id_usuario = usuarios.id_usuario JOIN estado ON formulas.id_estado = estado.id_estado WHERE formulas.id_formula = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            formulas = {'id': datos[0], 'control': datos[1],
                        'vigencia': datos[2], 'distancia': datos[3], 'lente': datos[4], 'filtro': datos[5], 'observacion': datos[6], 'tp_doc': datos[7], 'documento': datos[8], 'paciente': datos[9], 'usuario': datos[10], 'estado': datos[11]}
            return formulas
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el formulas por id desde end-point
@app.route('/formulas/<codigo>', methods=['GET'])
def leer_formula(codigo):
    try:
        formula = leer_formulas_bd(codigo)
        if formula != None:
            return jsonify({'formula': formula, 'mensaje': "formula encontrada.", 'exito': True})
        else:
            return jsonify({'mensaje': "formula no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar formulas en la base de datos via metodo POST HTTPS
@app.route('/formulas', methods=['POST'])
def registrar_formula():

    if (validar_fecha(request.json['control']) and validar_fecha(request.json['vigencia']) and validar_distancia(request.json['distancia'])):
        try:
            fecha_actual = datetime.today()
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO formulas (proximo_control, vigencia, distancia_pupilar, id_lente, id_filtro, observacion, fecha_mod, id_paciente, id_usuario, id_estado)
                VALUES ('{0}', '{1}', '{2}', {3}, {4}, '{5}', '{6}', {7}, {8}, {9})""".format(request.json['control'], request.json['vigencia'], request.json['distancia'], request.json['lente'], request.json['filtro'], request.json['observacion'], fecha_actual, request.json['paciente'], request.json['usuario'], request.json['estado'])
            cursor.execute(sql)
            # Confirma la acción de inserción.
            conexion.connection.commit()
            return jsonify({'mensaje': "Formula registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta para actualizar formulas en la base de datos via metodo PUT HTTPS
@app.route('/formulas/<codigo>', methods=['PUT'])
def actualizar_formulas(codigo):
    if (validar_fecha(request.json['control']) and validar_fecha(request.json['vigencia']) and validar_distancia(request.json['distancia'])):
        try:
            fecha_actual = datetime.today()
            formulas = leer_formulas_bd(codigo)
            if formulas != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE formulas SET proximo_control = '{0}', vigencia = '{1}', distancia_pupilar = '{2}', id_lente = {3}, id_filtro = {4}, observacion = '{5}', fecha_mod = '{6}', id_paciente = {7}, id_usuario = {8}, id_estado = {9}
                WHERE id_formula = {10} """.format(request.json['control'], request.json['vigencia'], request.json['distancia'], request.json['lente'], request.json['filtro'], request.json['observacion'], fecha_actual, request.json['paciente'], request.json['usuario'], request.json['estado'], codigo)
                cursor.execute(sql)
                # Confirma la acción de actualización.
                conexion.connection.commit()
                return jsonify({'mensaje': "Formula actualizada.", 'exito': True})
            else:
                return jsonify({'mensaje': "Formula no encontrada.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/formulas/<codigo>', methods=['DELETE'])
def eliminar_formula(codigo):
    try:
        formulas = leer_formulas_bd(codigo)
        if formulas != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM formulas WHERE id_formula = {0} ".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Formula eliminada.", 'exito': True})
        else:
            return jsonify({'mensaje': "Formula no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
