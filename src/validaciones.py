# Valida el código (si es numérico y de longitud 6).
def validar_codigo(codigo: str) -> bool:
    return (codigo.isnumeric() and len(codigo) == 6)


# Valida el nombre del usuario en el la cantidad de caracteres
def validar_nombre_usuario(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 50)


# Valida el nombre del paciente en el la cantidad de caracteres
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


# Valida el nombre del montura en el la cantidad de caracteres
def validar_montura(montura: str) -> bool:
    montura = montura.strip()
    return (len(montura) > 0 and len(montura) <= 50)
