from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

app = Flask(__name__)

# Cors activados para el consumo desde js app cliente
CORS(app, resources={r"/historias/*": {"origins": "http://localhost"}})

conexion = MySQL(app)


# ruta para listar todos los historias
@app.route('/historias', methods=['GET'])
def listar_historias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT hc.id_historial, (sintomas.nombre)sintomas, hc.ojo_derecho_vl_avsc, hc.ojo_derecho_vp_avsc, hc.ojo_derecho_ph_avsc, hc.ojo_izquierdo_vl_avsc, hc.ojo_izquierdo_vp_avsc, hc.ojo_izquierdo_ph_avsc, hc.ambos_vl_avsc, hc.ambos_vp_avsc, hc.ambos_ph_avsc, hc.ojo_derecho_vl_avcc, hc.ojo_derecho_vp_avcc, hc.ojo_derecho_ph_avcc, hc.ojo_izquierdo_vl_avcc, hc.ojo_izquierdo_vp_avcc, hc.ojo_izquierdo_ph_avcc, hc.ambos_vl_avcc, hc.ambos_vp_avcc, hc.ambos_ph_avcc, hc.ojo_derecho_ee, hc.ojo_izquierdo_ee, hc.observacion_reflejos, hc.vision_lejana_ct, hc.vision_proxima_ct, hc.observacion_motilidad, hc.observacion_punto, hc.ojo_derecho_of, hc.ojo_izquierdo_of, hc.ojo_derecho_qu, hc.ojo_izquierdo_qu, hc.ojo_derecho_refraccion, hc.ojo_izquierdo_refraccion,  hc.ojo_derecho_av_refraccion, hc.ojo_izquierdo_av_refraccion, hc.ojo_derecho_vl_rxf, hc.ojo_izquierdo_vl_rxf, hc.ojo_derecho_vp_rxf, hc.ojo_izquierdo_vp_rxf, hc.ojo_derecho_add_rxf, hc.ojo_izquierdo_add_rxf, hc.ojo_derecho_vc, hc.ojo_izquierdo_vc, hc.observacion_este, hc.fecha_mod, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM historia_clinica hc JOIN sintomas ON hc.id_sintomas = sintomas.id_sintoma JOIN paciente ON hc.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON hc.id_usuario = usuarios.id_usuario JOIN estado ON hc.id_estado = estado.id_estado ORDER BY hc.id_historial;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        historias = []
        for fila in datos:
            data = {'id': fila[0], 'sintoma': fila[1], 'ojo_derecho_vl_avsc': fila[2], 'ojo_derecho_vp_avsc': fila[3], 'ojo_derecho_ph_avsc': fila[4], 'ojo_izquierdo_vl_avsc': fila[5], 'ojo_izquierdo_vp_avsc': fila[6], 'ojo_izquierdo_ph_avsc': fila[7],
                    'ambos_vl_avsc': fila[8], 'ambos_vp_avsc': fila[9], 'ambos_ph_avsc': fila[10], 'ojo_derecho_vl_avcc': fila[11], 'ojo_derecho_vp_avcc': fila[12], 'ojo_derecho_ph_avcc': fila[13],
                    'ojo_izquierdo_vl_avcc': fila[14], 'ojo_izquierdo_vp_avcc': fila[15], 'ojo_izquierdo_ph_avcc': fila[16], 'ambos_vl_avcc': fila[17], 'ambos_vp_avcc': fila[18], 'ambos_ph_avcc': fila[19],
                    'ojo_derecho_ee': fila[20], 'ojo_izquierdo_ee': fila[21], 'observacion_reflejos': fila[22], 'vision_lejana_ct': fila[23], 'vision_proxima_ct': fila[24], 'observacion_motilidad': fila[25],
                    'observacion_punto': fila[26], 'ojo_derecho_of': fila[27], 'ojo_izquierdo_of': fila[28], 'ojo_derecho_qu': fila[29], 'ojo_izquierdo_qu': fila[30], 'ojo_derecho_refraccion': fila[31],
                    'ojo_izquierdo_refraccion': fila[32], 'ojo_derecho_av_refraccion': fila[33], 'ojo_izquierdo_av_refraccion': fila[34], 'ojo_derecho_vl_rxf': fila[35], 'ojo_izquierdo_vl_rxf': fila[36], 'ojo_derecho_vp_rxf': fila[37],
                    'ojo_izquierdo_vp_rxf': fila[38], 'ojo_derecho_add_rxf': fila[39], 'ojo_izquierdo_add_rxf': fila[40], 'ojo_derecho_vc': fila[41], 'ojo_izquierdo_vc': fila[42], 'observacion_este': fila[43],
                    'fecha_mod': fila[44], 'tp_doc': fila[45], 'documento': fila[46], 'paciente': fila[47], 'usuario': fila[48], 'estado': fila[49]}
            historias.append(data)
        return jsonify({'historias': historias, 'mensaje': "historias listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# consulta para listar un historia por id
def leer_historias_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT hc.id_historial, (sintomas.nombre)sintomas, hc.ojo_derecho_vl_avsc, hc.ojo_derecho_vp_avsc, hc.ojo_derecho_ph_avsc, hc.ojo_izquierdo_vl_avsc, hc.ojo_izquierdo_vp_avsc, hc.ojo_izquierdo_ph_avsc, hc.ambos_vl_avsc, hc.ambos_vp_avsc, hc.ambos_ph_avsc, hc.ojo_derecho_vl_avcc, hc.ojo_derecho_vp_avcc, hc.ojo_derecho_ph_avcc, hc.ojo_izquierdo_vl_avcc, hc.ojo_izquierdo_vp_avcc, hc.ojo_izquierdo_ph_avcc, hc.ambos_vl_avcc, hc.ambos_vp_avcc, hc.ambos_ph_avcc, hc.ojo_derecho_ee, hc.ojo_izquierdo_ee, hc.observacion_reflejos, hc.vision_lejana_ct, hc.vision_proxima_ct, hc.observacion_motilidad, hc.observacion_punto, hc.ojo_derecho_of, hc.ojo_izquierdo_of, hc.ojo_derecho_qu, hc.ojo_izquierdo_qu, hc.ojo_derecho_refraccion, hc.ojo_izquierdo_refraccion,  hc.ojo_derecho_av_refraccion, hc.ojo_izquierdo_av_refraccion, hc.ojo_derecho_vl_rxf, hc.ojo_izquierdo_vl_rxf, hc.ojo_derecho_vp_rxf, hc.ojo_izquierdo_vp_rxf, hc.ojo_derecho_add_rxf, hc.ojo_izquierdo_add_rxf, hc.ojo_derecho_vc, hc.ojo_izquierdo_vc, hc.observacion_este, hc.fecha_mod, (tipo_documento.nombre)tp_doc, paciente.documento, CONCAT(paciente.nombres, paciente.apellidos)paciente, (usuarios.nombre)usuario, estado.estado FROM historia_clinica hc JOIN sintomas ON hc.id_sintomas = sintomas.id_sintoma JOIN paciente ON hc.id_paciente = paciente.id_paciente JOIN tipo_documento ON paciente.id_documento = tipo_documento.id_documento JOIN usuarios ON hc.id_usuario = usuarios.id_usuario JOIN estado ON hc.id_estado = estado.id_estado WHERE hc.id_historial = '{0}'".format(
            codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            historias = {'id': datos[0], 'sintoma': datos[1], 'ojo_derecho_vl_avsc': datos[2], 'ojo_derecho_vp_avsc': datos[3], 'ojo_derecho_ph_avsc': datos[4], 'ojo_izquierdo_vl_avsc': datos[5], 'ojo_izquierdo_vp_avsc': datos[6], 'ojo_izquierdo_ph_avsc': datos[7],
                         'ambos_vl_avsc': datos[8], 'ambos_vp_avsc': datos[9], 'ambos_ph_avsc': datos[10], 'ojo_derecho_vl_avcc': datos[11], 'ojo_derecho_vp_avcc': datos[12], 'ojo_derecho_ph_avcc': datos[13],
                         'ojo_izquierdo_vl_avcc': datos[14], 'ojo_izquierdo_vp_avcc': datos[15], 'ojo_izquierdo_ph_avcc': datos[16], 'ambos_vl_avcc': datos[17], 'ambos_vp_avcc': datos[18], 'ambos_ph_avcc': datos[19],
                         'ojo_derecho_ee': datos[20], 'ojo_izquierdo_ee': datos[21], 'observacion_reflejos': datos[22], 'vision_lejana_ct': datos[23], 'vision_proxima_ct': datos[24], 'observacion_motilidad': datos[25],
                         'observacion_punto': datos[26], 'ojo_derecho_of': datos[27], 'ojo_izquierdo_of': datos[28], 'ojo_derecho_qu': datos[29], 'ojo_izquierdo_qu': datos[30], 'ojo_derecho_refraccion': datos[31],
                         'ojo_izquierdo_refraccion': datos[32], 'ojo_derecho_av_refraccion': datos[33], 'ojo_izquierdo_av_refraccion': datos[34], 'ojo_derecho_vl_rxf': datos[35], 'ojo_izquierdo_vl_rxf': datos[36], 'ojo_derecho_vp_rxf': datos[37],
                         'ojo_izquierdo_vp_rxf': datos[38], 'ojo_derecho_add_rxf': datos[39], 'ojo_izquierdo_add_rxf': datos[40], 'ojo_derecho_vc': datos[41], 'ojo_izquierdo_vc': datos[42], 'observacion_este': datos[43],
                         'fecha_mod': datos[44], 'tp_doc': datos[45], 'documento': datos[46], 'paciente': datos[47], 'usuario': datos[48], 'estado': datos[49]}
            return historias
        else:
            return None
    except Exception as ex:
        raise ex


# ruta para listar el historia por id desde end-point
@app.route('/historias/<codigo>', methods=['GET'])
def leer_historia(codigo):
    try:
        historia = leer_historias_bd(codigo)
        if historia != None:
            return jsonify({'historia': historia, 'mensaje': "historia encontrada.", 'exito': True})
        else:
            return jsonify({'mensaje': "historia no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para registrar historia en la base de datos via metodo POST HTTPS
@app.route('/historias', methods=['POST'])
def registrar_historia():
    try:
        fecha_actual = datetime.today()
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO historia_clinica (id_sintomas, ojo_derecho_vl_avsc, ojo_derecho_vp_avsc, ojo_derecho_ph_avsc, ojo_izquierdo_vl_avsc, ojo_izquierdo_vp_avsc, ojo_izquierdo_ph_avsc, ambos_vl_avsc, ambos_vp_avsc, ambos_ph_avsc, ojo_derecho_vl_avcc, ojo_derecho_vp_avcc, ojo_derecho_ph_avcc, ojo_izquierdo_vl_avcc, ojo_izquierdo_vp_avcc, ojo_izquierdo_ph_avcc, ambos_vl_avcc, ambos_vp_avcc, ambos_ph_avcc, ojo_derecho_ee, ojo_izquierdo_ee, observacion_reflejos, vision_lejana_ct, vision_proxima_ct, observacion_motilidad, observacion_punto, ojo_derecho_of, ojo_izquierdo_of, ojo_derecho_qu, ojo_izquierdo_qu, ojo_derecho_refraccion, ojo_izquierdo_refraccion, ojo_derecho_av_refraccion, ojo_izquierdo_av_refraccion, ojo_derecho_vl_rxf, ojo_izquierdo_vl_rxf, ojo_derecho_vp_rxf, ojo_izquierdo_vp_rxf, ojo_derecho_add_rxf, ojo_izquierdo_add_rxf, ojo_derecho_vc, ojo_izquierdo_vc, observacion_este, fecha_mod, id_paciente, id_usuario, id_estado)
            VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}', '{31}', '{32}', '{33}', '{34}', '{35}', '{36}', '{37}', '{38}', '{39}', '{40}', '{41}', '{42}', '{43}', {44}, {45}, {46})""".format(request.json['sintomas'], request.json['3'], request.json['4'], request.json['5'], request.json['6'], request.json['7'], request.json['8'], request.json['9'], request.json['10'], request.json['11'], request.json['12'], request.json['13'], request.json['14'], request.json['15'], request.json['16'], request.json['17'], request.json['18'], request.json['19'], request.json['20'], request.json['21'], request.json['22'], request.json['23'], request.json['24'], request.json['25'], request.json['26'], request.json['27'], request.json['28'], request.json['29'], request.json['30'], request.json['31'], request.json['32'], request.json['33'], request.json['34'], request.json['35'], request.json['36'], request.json['37'], request.json['38'], request.json['39'], request.json['40'], request.json['41'], request.json['42'], request.json['43'], request.json['44'], fecha_actual, request.json['paciente'], request.json['usuario'], request.json['estado'])
        cursor.execute(sql)
        # Confirma la acción de inserción.
        conexion.connection.commit()
        return jsonify({'mensaje': "Historia registrada.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta para actualizar historia en la base de datos via metodo PUT HTTPS
@app.route('/historias/<codigo>', methods=['PUT'])
def actualizar_historia(codigo):
    try:
        fecha_actual = datetime.today()
        historias = leer_historias_bd(codigo)
        if historias != None:
            cursor = conexion.connection.cursor()
            sql = """UPDATE historia_clinica SET id_sintomas = '{0}', ojo_derecho_vl_avsc = '{1}', ojo_derecho_vp_avsc = {2}, ojo_derecho_ph_avsc = {3}, ojo_izquierdo_vl_avsc = {4}, ojo_izquierdo_vp_avsc = {5}, ojo_izquierdo_ph_avsc = {6}, ambos_vl_avsc = {7}, ambos_vp_avsc = {8}, ambos_ph_avsc = {9}, ojo_derecho_vl_avcc = {10}, ojo_derecho_vp_avcc = {11}, ojo_derecho_ph_avcc = {12}, ojo_izquierdo_vl_avcc = {13}, ojo_izquierdo_vp_avcc = {14}, ojo_izquierdo_ph_avcc = {15}, ambos_vl_avcc = {16}, ambos_vp_avcc = {17}, ambos_ph_avcc = {18}, ojo_derecho_ee = {19}, ojo_izquierdo_ee = {20}, observacion_reflejos = {21}, vision_lejana_ct = {22}, vision_proxima_ct = {23}, observacion_motilidad = {24}, observacion_punto = {25}, ojo_derecho_of = {26}, ojo_izquierdo_of = {27}, ojo_derecho_qu = {28}, ojo_izquierdo_qu = {29}, ojo_derecho_refraccion = {30}, ojo_izquierdo_refraccion = {31}, ojo_derecho_av_refraccion = {32}, ojo_izquierdo_av_refraccion = {33}, ojo_derecho_vl_rxf = {34}, ojo_izquierdo_vl_rxf = {35}, ojo_derecho_vp_rxf = {36}, ojo_izquierdo_vp_rxf = {37}, ojo_derecho_add_rxf = {38}, ojo_izquierdo_add_rxf = {39}, ojo_derecho_vc = {40}, ojo_izquierdo_vc = {41}, observacion_este = {42}, fecha_mod = {43}, id_paciente = {44}, id_usuario = {45}, id_estado = {46}
                WHERE id_historial = {47} """.format(request.json['sintomas'], request.json['3'], request.json['4'], request.json['5'], request.json['6'], request.json['7'], request.json['8'], request.json['9'], request.json['10'], request.json['11'], request.json['12'], request.json['13'], request.json['14'], request.json['15'], request.json['16'], request.json['17'], request.json['18'], request.json['19'], request.json['20'], request.json['21'], request.json['22'], request.json['23'], request.json['24'], request.json['25'], request.json['26'], request.json['27'], request.json['28'], request.json['29'], request.json['30'], request.json['31'], request.json['32'], request.json['33'], request.json['34'], request.json['35'], request.json['36'], request.json['37'], request.json['38'], request.json['39'], request.json['40'], request.json['41'], request.json['42'], request.json['43'], request.json['44'], fecha_actual, request.json['paciente'], request.json['usuario'], request.json['estado'], codigo)
            cursor.execute(sql)
            # Confirma la acción de actualización.
            conexion.connection.commit()
            return jsonify({'mensaje': "Historia actualizada.", 'exito': True})
        else:
            return jsonify({'mensaje': "Historia no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


# ruta de eliminar registro en la base de datos via metodo DELETE HTTPS
@app.route('/historias/<codigo>', methods=['DELETE'])
def eliminar_historia(codigo):
    try:
        historias = leer_historias_bd(codigo)
        if historias != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM historia_clinica WHERE id_historial = {0} ".format(
                codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Historia eliminada.", 'exito': True})
        else:
            return jsonify({'mensaje': "Historia no encontrada.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1> Ruta inaccessible en API ☹ </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
