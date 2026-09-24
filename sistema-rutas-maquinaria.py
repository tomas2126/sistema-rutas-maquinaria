# ============================================================
# SISTEMA INTELIGENTE BASADO EN REGLAS
# Ruta de atención de fallas en maquinaria
# ============================================================
#
# Este programa representa un sistema sencillo de Inteligencia
# Artificial basado en conocimiento y reglas.
#
# El sistema recibe un tipo de falla de una máquina y, mediante
# reglas lógicas, determina la ruta que debe seguir para recibir
# atención.
#
# Proyecto académico - Inteligencia Artificial
# ============================================================


# ============================================================
# 1. BASE DE CONOCIMIENTO
# ============================================================
#
# La base de conocimiento contiene las diferentes fallas que
# el sistema puede reconocer y la información relacionada con
# cada una.
#
# Cada falla tiene:
# - Nombre de la falla.
# - Área encargada.
# - Técnico encargado.
# - Nivel de prioridad.
#
# En un sistema real esta información podría almacenarse en
# una base de datos. Para este ejercicio utilizaremos un
# diccionario de Python.

base_conocimiento = {

    "electrica": {
        "area": "Área eléctrica",
        "tecnico": "Técnico electricista",
        "prioridad": "Alta"
    },

    "mecanica": {
        "area": "Área mecánica",
        "tecnico": "Técnico mecánico",
        "prioridad": "Media"
    },

    "hidraulica": {
        "area": "Área hidráulica",
        "tecnico": "Técnico hidráulico",
        "prioridad": "Alta"
    },

    "neumatica": {
        "area": "Área neumática",
        "tecnico": "Técnico neumático",
        "prioridad": "Media"
    },

    "software": {
        "area": "Área de sistemas",
        "tecnico": "Técnico de sistemas",
        "prioridad": "Alta"
    }
}


# ============================================================
# 2. REGLAS DEL SISTEMA
# ============================================================
#
# Las reglas permiten relacionar el tipo de falla con el área
# que debe atenderla.
#
# Ejemplo:
#
# SI la falla es eléctrica
# ENTONCES la atención corresponde al área eléctrica.
#
# Estas reglas representan una forma sencilla de razonamiento
# basado en conocimiento.

reglas = {

    "electrica": "Si la falla es eléctrica, debe ser atendida por el área eléctrica.",

    "mecanica": "Si la falla es mecánica, debe ser atendida por el área mecánica.",

    "hidraulica": "Si la falla es hidráulica, debe ser atendida por el área hidráulica.",

    "neumatica": "Si la falla es neumática, debe ser atendida por el área neumática.",

    "software": "Si la falla está relacionada con software, debe ser atendida por el área de sistemas."
}


# ============================================================
# 3. FUNCIÓN PARA MOSTRAR LAS FALLAS DISPONIBLES
# ============================================================
#
# Esta función muestra al usuario las opciones que puede
# seleccionar.
#
# Una función permite organizar el código y evitar repetir
# instrucciones.

def mostrar_fallas():

    print("\nTipos de fallas disponibles:")

    for falla in base_conocimiento:
        print("-", falla.capitalize())


# ============================================================
# 4. FUNCIÓN DE BÚSQUEDA
# ============================================================
#
# Esta es una de las partes principales del sistema.
#
# La función recibe el tipo de falla y consulta la base de
# conocimiento.
#
# Si encuentra la falla:
# 1. Obtiene el área.
# 2. Obtiene el técnico.
# 3. Obtiene la prioridad.
# 4. Construye la ruta de atención.
#
# Si no encuentra la falla, informa que no existe una regla
# para atenderla.

def buscar_ruta(falla):

    # Convertimos el texto a minúsculas para facilitar
    # la comparación.
    falla = falla.lower().strip()

    # Verificamos si la falla existe en la base de conocimiento.
    if falla in base_conocimiento:

        informacion = base_conocimiento[falla]

        # Obtenemos los datos almacenados.
        area = informacion["area"]
        tecnico = informacion["tecnico"]
        prioridad = informacion["prioridad"]

        # Obtenemos la regla relacionada con la falla.
        regla = reglas[falla]

        # Construimos la ruta de atención.
        ruta = [
            "Máquina con falla",
            "Diagnóstico",
            area,
            tecnico,
            "Reparación"
        ]

        return ruta, prioridad, regla

    else:

        return None, None, None


# ============================================================
# 5. FUNCIÓN PARA MOSTRAR EL RESULTADO
# ============================================================
#
# Esta función recibe la información encontrada por el sistema
# y la presenta de una manera organizada para el usuario.

def mostrar_resultado(falla, ruta, prioridad, regla):

    print("\n==============================================")
    print("        RESULTADO DEL SISTEMA")
    print("==============================================")

    print("\nFalla identificada:", falla.capitalize())

    print("\nRegla aplicada:")
    print(regla)

    print("\nPrioridad de atención:", prioridad)

    print("\nRuta recomendada:")

    # enumerate permite mostrar el número de cada paso.
    for numero, paso in enumerate(ruta, start=1):
        print(f"{numero}. {paso}")

    print("\n==============================================")


# ============================================================
# 6. PROGRAMA PRINCIPAL
# ============================================================
#
# En esta sección comienza la interacción con el usuario.
#
# Primero mostramos las fallas disponibles.
# Después solicitamos al usuario que seleccione una.
# Finalmente ejecutamos la búsqueda.

print("================================================")
print(" SISTEMA INTELIGENTE DE ATENCIÓN DE MAQUINARIA")
print("================================================")

print("\nEste sistema determina una ruta de atención")
print("según el tipo de falla de una máquina.")

mostrar_fallas()

# Solicitamos la falla al usuario.
falla_usuario = input("\nIngrese el tipo de falla: ")

# Ejecutamos la búsqueda.
ruta, prioridad, regla = buscar_ruta(falla_usuario)


# ============================================================
# 7. VALIDACIÓN DEL RESULTADO
# ============================================================
#
# Si se encontró una ruta, mostramos el resultado.
# Si no se encontró, mostramos un mensaje indicando que
# el sistema no posee una regla para esa falla.

if ruta is not None:

    mostrar_resultado(
        falla_usuario,
        ruta,
        prioridad,
        regla
    )

else:

    print("\n==============================================")
    print("             RESULTADO")
    print("==============================================")

    print("\nNo se encontró una regla para la falla:",
          falla_usuario)

    print("\nLas opciones disponibles son:")

    mostrar_fallas()

    print("\n==============================================")