import json
# CONSTANTES

MAX_ESTUDIANTES = 1000
CANTIDAD_NOTAS = 5
NOTA_MIN = 1
NOTA_MAX = 10
LEGAJO_CIFRAS = 5
LEGAJO_MIN = 10000          
GENEROS_VALIDOS = ("F", "M", "X")   
LETRAS_VALIDAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚÜÑáéíóúüñ"

CAMPOS_CSV = 3 + CANTIDAD_NOTAS + 1

#VALIDACIONES

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
    Verifica que un texto represente un entero dentro de un rango (inclusive).

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

    Se controla el LARGO DEL TEXTO (no solo el valor) para rechazar casos
    como "01234", que como número valdría 1234 pero tiene ceros a la izquierda.

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
    Pide un entero por consola y repite hasta que esté en el rango indicado.

    Args:
        mensaje (str): texto que se muestra al pedir el dato.
        minimo (int): menor valor aceptado (inclusive).
        maximo (int): mayor valor aceptado (inclusive).

    Returns:
        int: el número ingresado, ya convertido y validado.
    """
    dato = input(mensaje).strip()
    while not validacion_entero_en_rango(dato, minimo, maximo):
        print(f"ERROR: ingresá un número entero entre {minimo} y {maximo}.")
        dato = input(mensaje).strip()
    return int(dato)

def pedir_legajo(mensaje: str = "Legajo (5 cifras): ") -> int:
    """
    Pide un legajo de 5 cifras y repite hasta que sea válido.

    Args:
        mensaje (str, opcional): texto a mostrar. Por defecto "Legajo (5 cifras): ".
            Se puede cambiar para reutilizar la función (ej: en la búsqueda).

    Returns:
        int: el legajo validado, convertido a entero.
    """
    dato = input(mensaje).strip()
    while not validacion_legajo(dato):
        print("ERROR: el legajo debe ser un número entero de 5 cifras (10000 a 99999).")
        dato = input(mensaje).strip()
    return int(dato)

def pedir_legajo_nuevo(estudiantes: list) -> int:
    """
    Pide un legajo válido que además NO exista ya en la lista.

    Evita legajos duplicados, ya que el legajo identifica a cada estudiante.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes cargados.

    Returns:
        int: un legajo válido y no repetido.
    """
    legajo = pedir_legajo()
    while buscar_estudiante(estudiantes, legajo) != -1:
        print("ERROR: ya existe un estudiante con ese legajo.")
        legajo = pedir_legajo()
    return legajo

def pedir_nombre() -> str:
    """
    Pide nombre y apellido (solo letras y espacios) y repite hasta que sea válido.

    Returns:
        str: el nombre validado, con formato Título (ej: "ana perez" -> "Ana Perez").
    """
    dato = input("Nombre y apellido: ").strip()
    while not validacion_nombre(dato):
        print("ERROR: solo se permiten letras y espacios.")
        dato = input("Nombre y apellido: ").strip()
    return dato.title()

def pedir_genero() -> str:
    """
    Pide el género (F, M o X). Acepta minúsculas y las pasa a mayúscula.

    Returns:
        str: 'F', 'M' o 'X'.
    """
    dato = input("Género (F / M / X): ").strip().upper()
    while not validacion_genero(dato):
        print("ERROR: ingresá F, M o X.")
        dato = input("Género (F / M / X): ").strip().upper()
    return dato

def pedir_nota(numero_materia: int) -> int:
    """
    Pide UNA nota (entero entre 1 y 10) de la materia indicada.

    Args:
        numero_materia (int): número de materia (1 a 5), solo para el mensaje.

    Returns:
        int: la nota validada.
    """
    mensaje = f"  Nota de MAT_{numero_materia} ({NOTA_MIN}-{NOTA_MAX}): "
    dato = input(mensaje).strip()
    while not validacion_nota(dato):
        print(f"  ERROR: la nota debe ser un entero entre {NOTA_MIN} y {NOTA_MAX}.")
        dato = input(mensaje).strip()
    return int(dato)

def pedir_notas() -> list:
    """
    Pide las CANTIDAD_NOTAS (5) notas, una por una.

    Returns:
        list: lista de 5 enteros, cada uno entre 1 y 10.
    """
    print("Notas:")
    notas = []
    for i in range(CANTIDAD_NOTAS):
        notas.append(pedir_nota(i + 1))
    return notas

def pedir_orden() -> str:
    """
    Pide el criterio de ordenamiento: 'ASC' (ascendente) o 'DESC' (descendente).

    Returns:
        str: 'ASC' o 'DESC' (acepta minúsculas y las convierte).
    """
    dato = input("Orden (ASC / DESC): ").strip().upper()
    while not validacion_orden(dato):
        print("ERROR: ingresá ASC o DESC.")
        dato = input("Orden (ASC / DESC): ").strip().upper()
    return dato

def crear_estudiante(legajo: int, nombre: str, genero: str, notas: list) -> dict:
    """
    Arma el diccionario de un estudiante.

    Args:
        legajo (int): legajo de 5 cifras (ya validado).
        nombre (str): nombre y apellido (ya validado).
        genero (str): 'F', 'M' o 'X' (ya validado).
        notas (list): lista de 5 enteros entre 1 y 10 (ya validada).

    Returns:
        dict: {"legajo", "nombre", "genero", "notas", "promedio"}.
    """
    return {
        "legajo": legajo,
        "nombre": nombre,
        "genero": genero,
        "notas": notas,
        "promedio": 0.0,
    }

# CARGAR DATOS

def linea_a_estudiante(linea: str):
    """
    Convierte UNA línea de texto del CSV en un diccionario de estudiante.

    Args:
        linea (str): una línea del archivo CSV.

    Returns:
        dict | None: el diccionario del estudiante si la línea es válida;
                     None si tiene mal la cantidad de campos o algún dato inválido.
    """
    campos = linea.strip().split(",")
    if len(campos) != CAMPOS_CSV:
        return None

    legajo_txt = campos[0].strip()
    nombre = campos[1].strip()
    genero = campos[2].strip().upper()

    if not validacion_legajo(legajo_txt):
        return None
    if not validacion_nombre(nombre):
        return None
    if not validacion_genero(genero):
        return None

    notas = []
    for texto in campos[3:3 + CANTIDAD_NOTAS]:
        texto = texto.strip()
        if not validacion_nota(texto):
            return None
        notas.append(int(texto))

    return crear_estudiante(int(legajo_txt), nombre.title(), genero, notas)

def cargar_desde_csv(estudiantes: list, ruta: str) -> None:
    """
    Carga los estudiantes desde un archivo CSV y REEMPLAZA el contenido de la lista.

    Se usa encoding "utf-8-sig" para leer bien tildes y ñ.

    Args:
        estudiantes (list): lista de diccionarios que se va a modificar.
        ruta (str): nombre o ruta del archivo CSV.

    Returns:
        None. Informa el resultado por pantalla.
    """
    nuevos = []
    try:
        with open(ruta, "r", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                if linea.strip() == "":
                    continue                      
                estudiante = linea_a_estudiante(linea)
                if estudiante is None:
                    print(f"  Línea ignorada (datos inválidos): {linea.strip()}")
                elif buscar_estudiante(nuevos, estudiante["legajo"]) != -1:
                    print(f"  Línea ignorada (legajo repetido): {linea.strip()}")
                elif len(nuevos) >= MAX_ESTUDIANTES:
                    print(f"  Línea ignorada (máximo de {MAX_ESTUDIANTES} alcanzado): {linea.strip()}")
                else:
                    nuevos.append(estudiante)
    except FileNotFoundError:
        print(f"ERROR: no se encontró el archivo '{ruta}'.")
        return
    except OSError:
        print(f"ERROR: no se pudo leer el archivo '{ruta}'.")
        return

    if len(nuevos) == 0:
        print("El archivo no tiene estudiantes válidos. No se modificó la lista.")
        return

    estudiantes.clear()
    estudiantes.extend(nuevos)
    print(f"Se cargaron {len(estudiantes)} estudiantes desde '{ruta}'.")


def cargar_manual(estudiantes: list) -> None:
    """
    Pide por teclado los datos de cada estudiantes y los AGREGA a la lista.

    Args:
        estudiantes (list): lista de diccionarios a la que se agregan los nuevos.

    Returns:
        None. Informa por pantalla cuántos se cargaron.
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

# CALCULOS

def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas (list): lista de enteros (las 5 notas de un estudiante).

    Returns:
        float: suma / cantidad, redondeado a 2 decimales.
    """
    suma = 0
    for nota in notas:
        suma += nota
    return round(suma / len(notas), 2)


def calcular_promedios(estudiantes: list) -> None:
    """
    Calcula el promedio de CADA estudiante y lo guarda en su clave "promedio".

    Modifica los diccionarios en el lugar (no retorna nada).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    for estudiante in estudiantes:
        estudiante["promedio"] = calcular_promedio(estudiante["notas"])


def ordenar_por_promedio(estudiantes: list, orden: str) -> None:
    """
    Ordena la lista de diccionarios por la clave "promedio".

    Args:
        estudiantes (list): lista de diccionarios; se ordena en el lugar.
        orden (str): 'ASC' (menor a mayor) o 'DESC' (mayor a menor).

    Returns:
        None.
    """
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if orden == "ASC":
                intercambiar = estudiantes[j]["promedio"] < estudiantes[i]["promedio"]
            else:
                intercambiar = estudiantes[j]["promedio"] > estudiantes[i]["promedio"]
            if intercambiar:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]


def sumar_notas_por_materia(estudiantes: list) -> list:
    """
    Suma todas las notas de cada materia, de todos los estudiantes.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        list: lista de 5 enteros. Índice 0 = suma de MAT_1, índice 1 = suma
              de MAT_2, y así sucesivamente.
    """
    sumas = [0] * CANTIDAD_NOTAS
    for estudiante in estudiantes:
        for i in range(CANTIDAD_NOTAS):
            sumas[i] += estudiante["notas"][i]
    return sumas


def contar_notas(estudiantes: list, indice_materia: int) -> list:
    """
    Cuenta cuántas veces aparece cada nota (1 a 10) en una materia.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.
        indice_materia (int): 0 para MAT_1, 1 para MAT_2, ..., 4 para MAT_5.

    Returns:
        list: lista de 10 enteros con la cantidad de apariciones de cada nota.
    """
    conteo = [0] * (NOTA_MAX - NOTA_MIN + 1)
    for estudiante in estudiantes:
        nota = estudiante["notas"][indice_materia]
        conteo[nota - NOTA_MIN] += 1
    return conteo

# BUSQUEDA

def buscar_estudiante(estudiantes: list, legajo: int) -> int:
    """
    Búsqueda secuencial de un estudiante por legajo.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.
        legajo (int): legajo a buscar.

    Returns:
        int: la posición (índice) del estudiante en la lista, o -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo:
            return i
    return -1


def hay_datos(estudiantes: list) -> bool:
    """
    Indica si ya hay al menos un estudiante cargado (base de la Nota 1).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        bool: True si la lista no está vacía.
    """
    return len(estudiantes) > 0


def promedios_calculados(estudiantes: list) -> bool:
    """
    Indica si TODOS los estudiantes tienen su promedio calculado.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        bool: True si ningún estudiante tiene promedio 0.
    """
    for estudiante in estudiantes:
        if estudiante["promedio"] == 0:
            return False
    return True

# MOSTRAR DATO

def mostrar_encabezado() -> None:
    """
    Muestra el encabezado de la tabla de estudiantes:
    LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM

    Returns:
        None.
    """
    print(f"{'LEGAJO':<8}| {'NOMBRE':<22}| {'GENERO':<7}| N1 | N2 | N3 | N4 | N5 | PROM")
    print("-" * 78)


def mostrar_estudiante(estudiante: dict) -> None:
    """
    Muestra los datos de UN estudiante en una sola línea, alineados con el encabezado.

    Args:
        estudiante (dict): diccionario con legajo, nombre, genero, notas y promedio.

    Returns:
        None.
    """
    print(
        f"{estudiante['legajo']:<8}| {estudiante['nombre']:<22}| {estudiante['genero']:<7}|",
        end="",
    )
    for nota in estudiante["notas"]:
        print(f" {nota:>2} |", end="")
    print(f" {estudiante['promedio']:.2f}")


def mostrar_estudiantes(estudiantes: list) -> None:
    """
    Muestra el encabezado y TODOS los estudiantes.

    Recorre la lista con un for y, por cada elemento, llama a mostrar_estudiante().

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    mostrar_encabezado()
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Muestra UNA materia con su promedio general.

    El nombre de la materia es "MAT_" + (índice + 1): índice 0 -> MAT_1.

    Args:
        indice (int): índice de la materia (0 a 4).
        promedio (float): promedio general de esa materia.

    Returns:
        None.
    """
    print(f"MAT_{indice + 1}: {promedio:.2f}")


def mostrar_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Recorre las materias y muestra la/s de mayor promedio general.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes (no vacía).

    Returns:
        None.
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
    Muestra cuántas veces se repite cada nota (1 a 10) en una materia.

    Args:
        conteo (list): lista de 10 enteros devuelta por contar_notas().
        indice_materia (int): índice de la materia (0 a 4), para el título.

    Returns:
        None.
    """
    print(f"\nRepetición de notas en MAT_{indice_materia + 1}:")
    for i in range(len(conteo)):
        print(f"  Nota {i + NOTA_MIN:>2}: {conteo[i]} vez/veces")

# GUARDADO EN JSON

def guardar_json(estudiantes: list, ruta: str) -> bool:
    """
    Guarda la lista de diccionarios completa en un archivo JSON.

    Args:
        estudiantes (list): lista de diccionarios a guardar.
        ruta (str): nombre o ruta del archivo JSON de destino.

    Returns:
        bool: True si se guardó correctamente; False si hubo un error al
              escribir (por ejemplo, ruta inexistente o sin permisos).
    """
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
    except OSError:
        return False
    return True
