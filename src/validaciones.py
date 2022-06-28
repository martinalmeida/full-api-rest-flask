from datetime import datetime


# Valida el nombre del usuario en la cantidad de caracteres
def validar_nombre_usuario(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 50)


# Valida el nombre del paciente en la cantidad de caracteres
def validar_nombre_paciente(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 100)


# Valida el documento en la cantidad de caracteres
def validar_documento(documento: str) -> bool:
    documento = documento.strip()
    return (len(documento) > 0 and len(documento) <= 20)


# Valida el celular en la cantidad de caracteres
def validar_celular(celular: str) -> bool:
    celular = celular.strip()
    return (len(celular) > 0 and len(celular) <= 10)


# Valida el nombre del montura en la cantidad de caracteres
def validar_montura(montura: str) -> bool:
    montura = montura.strip()
    return (len(montura) > 0 and len(montura) <= 50)


# Valida el nombre del sintoma en la cantidad de caracteres
def validar_sintoma(sintoma: str) -> bool:
    sintoma = sintoma.strip()
    return (len(sintoma) > 0 and len(sintoma) <= 50)


# Valida el formato de fecha
def validar_fecha(fecha: str) -> bool:
    try:
        return datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        return False


# Valida el valor de cotizacion en la cantidad de caracteres
def validar_valor(cotizacion: str) -> bool:
    cotizacion = cotizacion.strip()
    return (len(cotizacion) > 0 and len(cotizacion) <= 10)


# Valida el valor de distancia en la cantidad de caracteres
def validar_distancia(distancia: str) -> bool:
    distancia = distancia.strip()
    return (len(distancia) > 0 and len(distancia) <= 50)
