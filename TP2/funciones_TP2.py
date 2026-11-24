# CONSTANTES

MAX_ESTUDIANTES = 1000
CANTIDAD_NOTAS = 5
NOTA_MIN = 1
NOTA_MAX = 10
LEGAJO_CIFRAS = 5
LEGAJO_MIN = 10000          
GENEROS_VALIDOS = ("F", "M", "X")   
LETRAS_VALIDAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚÜÑáéíóúüñ"


DATOS_HARCODEADOS = (
    (10001, "Ana Perez", "F", [8, 9, 7, 10, 6]),
    (10002, "Juan Gomez", "M", [5, 6, 7, 8, 9]),
    (10003, "Luca Diaz", "X", [10, 10, 9, 9, 8]),
    (10004, "María López", "F", [4, 7, 8, 6, 5]),
    (10005, "Pedro Ruiz", "M", [9, 8, 10, 7, 9]),
    (10006, "Sofia Castro", "F", [6, 6, 6, 6, 6]),
    (10007, "Nicolas Vega", "M", [7, 9, 5, 8, 10]),
    (10008, "Camila Rios", "F", [3, 5, 4, 7, 6]),
    (10009, "Tomas Silva", "M", [8, 7, 9, 10, 8]),
    (10010, "Valen Torres", "X", [10, 9, 8, 7, 6]),
)


# VALIDACIONES 

def solo_digitos(dato: str) -> bool:
    """
    Verifica que un texto no esté vacío y contenga únicamente dígitos (0-9).

    Args:
        dato (str): texto a evaluar.

    Returns:
        bool: True si el texto tiene al menos un carácter y todos son dígitos;
              False si está vacío o contiene cualquier otro carácter
              (letras, espacios, signos, punto decimal, signo menos).
    """
    if dato == "":
        return False
    for c in dato:
        if not "0" <= c <= "9":
            return False
    return True


def validacion_entero_en_rango(dato: str, minimo: int, maximo: int) -> bool:
    """
    Verifica que un texto represente un entero dentro de un rango.
    Es la validación base: la reutilizan la validación de notas y la del menú.

    Args:
        dato (str): texto a evaluar.
        minimo (int): menor valor permitido (inclusive).
        maximo (int): mayor valor permitido (inclusive).

    Returns:
        bool: True si el texto es un entero y minimo <= entero <= maximo.
    """
    if not solo_digitos(dato):
        return False
    return minimo <= int(dato) <= maximo


def validacion_legajo(dato: str) -> bool:
    """
    Verifica que el legajo sea un entero de exactamente 5 cifras.

    Args:
        dato (str): legajo ingresado como texto.

    Returns:
        bool: True si son 5 dígitos y el valor es >= 10000.
    """
    if not solo_digitos(dato):
        return False
    return len(dato) == LEGAJO_CIFRAS and int(dato) >= LEGAJO_MIN


def validacion_nombre(texto: str) -> bool:
    """
    Verifica que el nombre contenga solo letras (con tildes y ñ) y espacios,
    y que tenga al menos una letra.

    Args:
        texto (str): nombre y apellido ingresado.

    Returns:
        bool: True si todos los caracteres son letras válidas o espacios y
              hay al menos una letra; False en caso contrario.
    """
    hay_letra = False
    for caracter in texto:
        if caracter in LETRAS_VALIDAS:
            hay_letra = True
        elif caracter != " ":
            return False
    return hay_letra


def validacion_genero(dato: str) -> bool:
    """
    Verifica que el género sea uno de los permitidos: 'F', 'M' o 'X'.

    Distingue mayúsculas de minúsculas: la conversión a mayúscula se hace
    antes de llamar a esta función (ver pedir_genero).

    Args:
        dato (str): género ingresado.

    Returns:
        bool: True si el dato está en GENEROS_VALIDOS.
    """
    return dato in GENEROS_VALIDOS


def validacion_nota(dato: str) -> bool:
    """
    Verifica que una nota sea un entero entre NOTA_MIN (1) y NOTA_MAX (10).

    Args:
        dato (str): nota ingresada como texto.

    Returns:
        bool: True si es un entero entre 1 y 10 inclusive.
    """
    return validacion_entero_en_rango(dato, NOTA_MIN, NOTA_MAX)


def validacion_orden(dato: str) -> bool:
    """
    Verifica que el criterio de ordenamiento sea 'ASC' o 'DESC'.

    Args:
        dato (str): orden ingresado (ya en mayúsculas).

    Returns:
        bool: True si es exactamente 'ASC' o 'DESC'.
    """
    return dato == "ASC" or dato == "DESC"

# PEDIDO DE DATOS 

def pedir_entero_en_rango(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Solicita un número entero dentro de un rango y repite el pedido hasta que sea válido.

    Args:
        mensaje (str): texto que se muestra para solicitar el dato.
        minimo (int): valor mínimo permitido.
        maximo (int): valor máximo permitido.

    Returns:
        int: número entero ingresado dentro del rango indicado."""
    
    dato = input(mensaje).strip()
    while not validacion_entero_en_rango(dato, minimo, maximo):
        print(f"ERROR: ingresá un número entero entre {minimo} y {maximo}.")
        dato = input(mensaje).strip()
    return int(dato)


def pedir_legajo(mensaje: str = "Legajo (5 cifras): ") -> int:
    """
    Solicita un legajo válido de cinco cifras y lo convierte a entero.

    Args:
        mensaje (str): texto que se muestra para solicitar el legajo.

    Returns:
        int: legajo ingresado, comprendido entre 10000 y 99999.
    """

    dato = input(mensaje).strip()
    while not validacion_legajo(dato):
        print("ERROR: el legajo debe ser un número entero de 5 cifras (10000 a 99999).")
        dato = input(mensaje).strip()
    return int(dato)


def pedir_legajo_nuevo(estudiantes: list) -> int:
    """
    Solicita un legajo válido y comprueba que no esté registrado en la lista.

    Args:
        estudiantes (list): lista de diccionarios con los estudiantes cargados.

    Returns:
        int: legajo ingresado que no pertenece a otro estudiante.
    """

    legajo = pedir_legajo()
    while buscar_estudiante(estudiantes, legajo) != -1:
        print("ERROR: ya existe un estudiante con ese legajo.")
        legajo = pedir_legajo()
    return legajo


def pedir_nombre() -> str:
    """
    Solicita un nombre y apellido compuestos únicamente por letras y espacios.

    Returns:
        str: nombre y apellido validados, con la primera letra de cada palabra en mayúscula
    """
    dato = input("Nombre y apellido: ").strip()
    while not validacion_nombre(dato):
        print("ERROR: solo se permiten letras y espacios.")
        dato = input("Nombre y apellido: ").strip()
    return dato.title()


def pedir_genero() -> str:
    """
    Solicita y valida el género del estudiante. Acepta F, M o X, sin distinguir mayúsculas.

    Returns:
        str: letra que representa el género, convertida a mayúscula.
    """

    dato = input("Género (F / M / X): ").strip().upper()
    while not validacion_genero(dato):
        print("ERROR: ingresá F, M o X.")
        dato = input("Género (F / M / X): ").strip().upper()
    return dato


def pedir_nota(numero_materia: int) -> int:
    """
    Solicita y valida la nota de una materia, como un entero entre NOTA_MIN y NOTA_MAX.

    Args:
        numero_materia (int): número de la materia cuya nota se solicita.

    Returns:
        int: nota ingresada dentro del rango permitido.
    """
    mensaje = f"  Nota de MAT_{numero_materia} ({NOTA_MIN}-{NOTA_MAX}): "
    dato = input(mensaje).strip()
    while not validacion_nota(dato):
        print(f"  ERROR: la nota debe ser un entero entre {NOTA_MIN} y {NOTA_MAX}.")
        dato = input(mensaje).strip()
    return int(dato)


def pedir_notas() -> list:
    """
    Solicita las notas de todas las materias, una por una.

    Returns:
        list: lista con las notas ingresadas y validadas
    """
    print("Notas:")
    notas = []
    for i in range(CANTIDAD_NOTAS):
        notas.append(pedir_nota(i + 1))
    return notas


def pedir_orden() -> str:
    """
    Solicita y valida el criterio de ordenamiento de la lista de estudiantes.

    Returns:
        str: "ASC" para ordenar de menor a mayor o "DESC" para ordenar de mayor a menor.
    """

    dato = input("Orden (ASC / DESC): ").strip().upper()
    while not validacion_orden(dato):
        print("ERROR: ingresá ASC o DESC.")
        dato = input("Orden (ASC / DESC): ").strip().upper()
    return dato


def pedir_opcion_menu() -> int:
    """
    Solicita y valida una opción del menú principal, comprendida entre 1 y 8.

    Returns:
        int: número de la opción seleccionada.
    """
    return pedir_entero_en_rango("Elegí una opción: ", 1, 8)


# CREACIÓN Y CARGA

def crear_estudiante(legajo: int, nombre: str, genero: str, notas: list) -> dict:
    """
    Crea y retorna el diccionario que contiene los datos de un estudiante.
    El promedio se inicializa en 0.0 y se calcula posteriormente desde la opción 3 del menú.

    Args:
        legajo (int): número de legajo del estudiante.
        nombre (str): nombre y apellido del estudiante.
        genero (str): género del estudiante (F, M o X).
        notas (list): lista de notas correspondientes a las materias.

    Returns:
        dict: diccionario con las claves LEGAJO, NOMBRE, GENERO, NOTAS y PROMEDIO.
    """
    return {
        "LEGAJO": legajo,
        "NOMBRE": nombre,
        "GENERO": genero,
        "NOTAS": notas,
        "PROMEDIO": 0.0,
    }


def cargar_manual(estudiantes: list) -> None:
    """
    Solicita por teclado los datos de uno o más estudiantes y los agrega a la lista.
    La cantidad ingresada está limitada por el máximo de estudiantes permitido.

    Args:
        estudiantes (list): lista donde se agregan los nuevos estudiantes.

    Returns:
        None: no retorna ningún valor; modifica la lista recibida.
    """
    lugar = MAX_ESTUDIANTES - len(estudiantes)
    if lugar == 0:
        print(f"Ya se alcanzó el máximo de {MAX_ESTUDIANTES} estudiantes.")
        return

    cantidad = pedir_entero_en_rango(
        f"¿Cuántos estudiantes querés cargar? (1 a {lugar}): ", 1, lugar
    )
    for i in range(cantidad):
        print(f"\n--- Estudiante {i + 1} de {cantidad} ---")
        legajo = pedir_legajo_nuevo(estudiantes)
        nombre = pedir_nombre()
        genero = pedir_genero()
        notas = pedir_notas()
        estudiantes.append(crear_estudiante(legajo, nombre, genero, notas))

    print(f"\nSe cargaron {cantidad} estudiantes. Total en la lista: {len(estudiantes)}")


def cargar_datos_prueba(estudiantes: list) -> None:
    """
     Reemplaza el contenido de la lista por los estudiantes definidos en DATOS_HARDCODEADOS.
    Limpia la lista existente y agrega los nuevos diccionarios, conservando la misma lista.

    Args:
        estudiantes (list): lista que se reemplaza por los datos de prueba.

    Returns:
        None: no retorna ningún valor; modifica la lista recibida.
    """
    estudiantes.clear()
    for legajo, nombre, genero, notas in DATOS_HARCODEADOS: 
        estudiantes.append(crear_estudiante(legajo, nombre, genero, notas.copy()))
    print(f"Se cargaron {len(estudiantes)} estudiantes de prueba.")


# CÁLCULOS

def calcular_promedio(notas: list) -> float:
    """Calcula el promedio aritmético de las notas y redondea el resultado a dos decimales.

    Args:
        notas (list): lista de notas que se utilizan para calcular el promedio.

    Returns:
        float: promedio de las notas, redondeado a dos decimales."""
    suma = 0
    for nota in notas:
        suma += nota
    return round(suma / len(notas), 2)


def calcular_promedios(estudiantes: list) -> None:
    """ Calcula el promedio de cada estudiante y lo almacena en la clave PROMEDIO de su diccionario.

    Args:
        estudiantes (list): lista de diccionarios con los datos de los estudiantes.

    Returns:
        None: no retorna ningún valor; actualiza el promedio de cada estudiante."""
    for estudiante in estudiantes:
        estudiante["PROMEDIO"] = calcular_promedio(estudiante["NOTAS"])


def ordenar_por_promedio(estudiantes: list, orden: str) -> None:
    """
    Ordena la lista de estudiantes según el valor de la clave PROMEDIO.
    Utiliza el método de intercambio directo para ordenar de forma ascendente o descendente.

    Args:
        estudiantes (list): lista de diccionarios que se va a ordenar.
        orden (str): criterio de ordenamiento; "ASC" (menor a mayor) o "DESC" (mayor a menor).

    Returns:
        None: no retorna ningún valor; modifica el orden de los elementos de la lista.
    """
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if orden == "ASC":
                intercambiar = estudiantes[j]["PROMEDIO"] < estudiantes[i]["PROMEDIO"]
            else:
                intercambiar = estudiantes[j]["PROMEDIO"] > estudiantes[i]["PROMEDIO"]
            if intercambiar:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]


def sumar_notas_por_materia(estudiantes: list) -> list:
    """
    Suma las notas de todos los estudiantes para cada una de las materias.

    Args:
        estudiantes (list): lista de diccionarios con las notas de los estudiantes.

    Returns:
        list: lista de sumas por materia; cada posición corresponde a MAT_1, MAT_2 y así sucesivamente
    """
    sumas = [0] * CANTIDAD_NOTAS
    for estudiante in estudiantes:
        for i in range(CANTIDAD_NOTAS):
            sumas[i] += estudiante["NOTAS"][i]
    return sumas


def contar_notas(estudiantes: list, indice_materia: int) -> list:
    """
    Cuenta la cantidad de veces que aparece cada nota en la materia indicada.

    Args:
        estudiantes (list): lista de diccionarios con las notas de los estudiantes.
        indice_materia (int): índice de la materia (0 = MAT_1, 1 = MAT_2, etc.).

    Returns:
        list: lista de 10 elementos con la cantidad de veces que aparece cada nota.
    """
    conteo = [0] * (NOTA_MAX - NOTA_MIN + 1)
    for estudiante in estudiantes:
        nota = estudiante["NOTAS"][indice_materia]
        conteo[nota - NOTA_MIN] += 1
    return conteo

# BÚSQUEDA Y CONTROLES DE ACCESO

def buscar_estudiante(estudiantes: list, legajo: int) -> int:
    """
    Busca en la lista al estudiante que tenga el legajo indicado.

    Args:
        estudiantes (list): lista de diccionarios donde se realiza la búsqueda.
        legajo (int): número de legajo que se desea encontrar.

    Returns:
        int: índice del estudiante encontrado o -1 si no existe en la lista.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["LEGAJO"] == legajo:
            return i
    return -1


def hay_datos(estudiantes: list) -> bool:
    """
    Comprueba si la lista contiene al menos un estudiante.

    Args:
        estudiantes (list): lista de estudiantes que se desea comprobar.

    Returns:
        bool: True si la lista contiene uno o más estudiantes; False si está vacía.
    """
    return len(estudiantes) > 0


def promedios_calculados(estudiantes: list) -> bool:
    """
    Comprueba si todos los estudiantes tienen calculado su promedio.
    Considera que un promedio igual a 0 indica que todavía no fue calculado.

    Args:
        estudiantes (list): lista de diccionarios que se desea comprobar.

    Returns:
        bool: True si todos los promedios están calculados; False si alguno vale 0.
    """
    for estudiante in estudiantes:
        if estudiante["PROMEDIO"] == 0:
            return False
    return True


def acceso_permitido(opcion: int, estudiantes: list) -> bool:
    """
    Comprueba si se cumplen los requisitos para ingresar a la opción seleccionada del menú.

    Args:
        opcion (int): número de la opción del menú que se desea ejecutar.
        estudiantes (list): lista de estudiantes cargados en el programa.

    Returns:
        bool: True si se permite ingresar a la opción; False si no se cumplen los requisitos.
    """
    if opcion in (2, 3, 4, 5, 6, 7) and not hay_datos(estudiantes):
        print("\nERROR: primero tenés que cargar los datos (opción 1).")
        return False
    if opcion in (4, 6) and not promedios_calculados(estudiantes):
        print("\nERROR: primero tenés que calcular los promedios (opción 3).")
        return False
    return True


# MOSTRAR DATOS

def mostrar_menu() -> None:
    """
    Muestra las opciones del menú principal.
    """

    print("\n========== MENÚ DE ESTUDIANTES ==========")
    print("1 - Cargar los datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular el promedio de cada estudiante")
    print("4 - Ordenar y mostrar por promedio")
    print("5 - Mostrar la/s materia/s con mayor promedio general")
    print("6 - Buscar un estudiante por legajo")
    print("7 - Contar cuántas veces se repite cada nota en una materia")
    print("8 - Salir")


def mostrar_encabezado() -> None:
    """
    Muestra en pantalla los nombres de las columnas de la tabla de estudiantes.

    Returns:
        None: no retorna ningún valor; únicamente imprime el encabezado
    """
    print(f"{'LEGAJO':<8}| {'NOMBRE':<22}| {'GENERO':<7}| N1 | N2 | N3 | N4 | N5 | PROM")
    print("-" * 78)


def mostrar_estudiante(estudiante: dict) -> None:
    """
    Muestra en una sola línea los datos personales, las notas y el promedio de un estudiante.

    Args:
        estudiante (dict): diccionario con los datos del estudiante que se desea mostrar.

    Returns:
        None: no retorna ningún valor; imprime los datos en pantalla.
    """
    print(
        f"{estudiante['LEGAJO']:<8}| {estudiante['NOMBRE']:<22}| {estudiante['GENERO']:<7}|",
        end="",
    )
    for nota in estudiante["NOTAS"]:
        print(f" {nota:>2} |", end="")
    print(f" {estudiante['PROMEDIO']:.2f}")


def mostrar_estudiantes(estudiantes: list) -> None:
    """
    Muestra el encabezado de la tabla y los datos de todos los estudiantes de la lista.

    Args:
        estudiantes (list): lista de diccionarios con los estudiantes que se desean mostrar.

    Returns:
        None: no retorna ningún valor; imprime la información en pantalla.
    """
    mostrar_encabezado()
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Muestra el número de una materia y su promedio general con dos decimales.

    Args:
        indice (int): índice de la materia, comenzando en 0 para MAT_1.
        promedio (float): promedio general de la materia.

    Returns:
        None: no retorna ningún valor; imprime los datos de la materia.
    """
    print(f"MAT_{indice + 1}: {promedio:.2f}")


def mostrar_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Calcula y muestra la o las materias que tienen el mayor promedio general.
    Compara las sumas de las notas para identificar los empates sin depender del redondeo.

    Args:
        estudiantes (list): lista de diccionarios con las notas de los estudiantes.

    Returns:
        None: no retorna ningún valor; muestra en pantalla las materias con el mayor promedio.
    """
    sumas = sumar_notas_por_materia(estudiantes)
    mayor = sumas[0]
    for suma in sumas:
        if suma > mayor:
            mayor = suma

    print("Materia/s con mayor promedio general:")
    for i in range(len(sumas)):
        if sumas[i] == mayor:
            mostrar_materia(i, sumas[i] / len(estudiantes))


def mostrar_conteo_notas(conteo: list, indice_materia: int) -> None:
    """
    Muestra la cantidad de veces que aparece cada nota en la materia indicada.

    Args:
        conteo (list): lista con la cantidad de apariciones de cada nota, desde 1 hasta 10.
        indice_materia (int): índice de la materia que se muestra, comenzando en 0 para MAT_1.

    Returns:
        None: no retorna ningún valor; imprime el conteo de notas en pantalla
    """
    print(f"\nRepetición de notas en MAT_{indice_materia + 1}:")
    for i in range(len(conteo)):
        print(f"  Nota {i + NOTA_MIN:>2}: {conteo[i]} vez/veces")


# ÍTEMS DEL MENÚ 

def opcion_cargar_datos(estudiantes: list) -> None:
    """
    Ejecuta la opción 1 del menú y permite elegir entre la carga manual o los datos de prueba.

    Args:
        estudiantes (list): lista donde se cargan o reemplazan los datos de los estudiantes.

    Returns:
        None: no retorna ningún valor; ejecuta el método de carga seleccionado.
    """
    print("\n--- CARGA DE DATOS ---")
    print("1 - Cargar estudiantes manualmente")
    print("2 - Cargar datos de prueba (hardcodeados)")
    modo = pedir_entero_en_rango("Elegí cómo cargar: ", 1, 2)
    match modo:
        case 1:
            cargar_manual(estudiantes)
        case 2:
            cargar_datos_prueba(estudiantes)


def opcion_mostrar_datos(estudiantes: list) -> None:
    """
     Ejecuta la opción 2 del menú y muestra todos los estudiantes cargados.

    Args:
        estudiantes (list): lista de diccionarios con los estudiantes que se desean mostrar.

    Returns:
        None: no retorna ningún valor; imprime la lista de estudiantes
    """
    print("\n--- LISTA DE ESTUDIANTES ---")
    mostrar_estudiantes(estudiantes)


def opcion_calcular_promedios(estudiantes: list) -> None:
    """
     Ejecuta la opción 3 del menú y calcula y guarda el promedio de cada estudiante.

    Args:
        estudiantes (list): lista de diccionarios cuyos promedios se van a calcular.

    Returns:
        None: no retorna ningún valor; actualiza los promedios e informa el resultado.
    """
    calcular_promedios(estudiantes)
    print(f"\nPromedios calculados y guardados para {len(estudiantes)} estudiantes.")


def opcion_ordenar_por_promedio(estudiantes: list) -> None:
    """
    Ejecuta la opción 4 del menú, solicita el criterio de ordenamiento y muestra la lista ordenada.

    Args:
        estudiantes (list): lista de diccionarios que se va a ordenar y mostrar.

    Returns:
        None: no retorna ningún valor; modifica el orden de la lista y muestra sus elementos
    """
    print("\n--- ORDENAR POR PROMEDIO ---")
    orden = pedir_orden()
    ordenar_por_promedio(estudiantes, orden)
    print()
    mostrar_estudiantes(estudiantes)


def opcion_materia_mayor_promedio(estudiantes: list) -> None:
    """
    Ejecuta la opción 5 del menú y muestra la o las materias con mayor promedio general.

    Args:
        estudiantes (list): lista de diccionarios utilizada para calcular los promedios por materia.

    Returns:
        None: no retorna ningún valor; muestra las materias correspondientes.
    """
    print()
    mostrar_materias_mayor_promedio(estudiantes)


def opcion_buscar_por_legajo(estudiantes: list) -> None:
    """
    Ejecuta la opción 6 del menú y busca un estudiante por legajo, mostrando todos sus datos.

    Args:
        estudiantes (list): lista de diccionarios con los estudiantes disponibles.

    Returns:
        None: no retorna ningún valor; muestra los datos del estudiante encontrado o un mensaje de error.
    """
    print("\n--- BUSCAR POR LEGAJO ---")
    legajo = pedir_legajo("Legajo a buscar: ")
    posicion = buscar_estudiante(estudiantes, legajo)
    if posicion == -1:
        print(f"No se encontró ningún estudiante con el legajo {legajo}.")
    else:
        print("\nEstudiante encontrado:")
        mostrar_encabezado()
        mostrar_estudiante(estudiantes[posicion])


def opcion_contar_notas(estudiantes: list) -> None:
    """
    Ejecuta la opción 7 del menú y cuenta cuántas veces se repite cada nota en una materia.

    Args:
        estudiantes (list): lista de diccionarios con los estudiantes disponibles.

    Returns:
        None: no retorna ningún valor; muestra el conteo de notas para la materia seleccionada.
    """
    print("\n--- REPETICIÓN DE NOTAS POR MATERIA ---")
    numero = pedir_entero_en_rango(f"Materia (1 a {CANTIDAD_NOTAS}): ", 1, CANTIDAD_NOTAS)
    indice = numero - 1
    conteo = contar_notas(estudiantes, indice)
    mostrar_conteo_notas(conteo, indice)