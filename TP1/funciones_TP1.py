#FUNCIONES DE LISTAS Y MATRIZ

def crear_lista(cantidad:int, valor_inicial=0) -> list:
    '''
    Crea una lista de tamaño fijo con todos sus elementos iguales.

    Parámetros:
        cantidad (int): cantidad de elementos que tendrá la lista.
        valor_inicial (any): valor con el que se rellena cada posición.
                             Por defecto es 0.

    Retorna:
        list: lista de 'cantidad' elementos, todos con 'valor_inicial'.

    '''
    lista = [valor_inicial] * cantidad
    return lista

def crear_matriz(filas:int, columnas:int, valor_inicial=0) -> list:
    '''
    Crea una matriz (lista de listas) de 'filas' x 'columnas'.

    Parámetros:
        filas (int): cantidad de filas (estudiantes).
        columnas (int): cantidad de columnas (materias).
        valor_inicial (any): valor con el que se rellena cada celda.
                             Por defecto es 0.

    Retorna:
        list: matriz de filas x columnas.
    '''
    matriz = []
    for i in range(filas):
        fila = [valor_inicial] * columnas
        matriz.append(fila)
    
    return matriz

#VALIDACIONES DE LOS DATOS

def solo_digitos_numerico(dato: str) -> bool:
    '''
    Verifica que un texto no esté vacío y contenga únicamente dígitos (0-9).
    No admite espacios, signos ni decimales.

    Parámetros:
        dato (str): texto a verificar.

    Retorna:
        bool: True si todos los caracteres son dígitos, False en caso
              contrario o si el texto está vacío.
    '''
    if dato == "":
        return False
    for c in dato:
        if not "0" <= c <= "9":
            return False
    return True

def validar_legajo(dato:str) -> bool:
    '''
    Valida que el dato sea un legajo: un entero de exactamente cinco cifras.

    Parámetros:
        dato (str): texto ingresado por el usuario.

    Retorna:
        bool: True si es numérico, tiene 5 caracteres y no empieza con 0.

    '''
    return solo_digitos_numerico(dato) and len(dato) == 5 and int(dato) >= 10000

def legajo_repetido(legajo: int, legajos: list, cantidad: int) -> bool:
    '''
    Verifica si un legajo ya fue cargado. Corta apenas lo
    encuentra.

    Parámetros:
        legajo (int): legajo a verificar.
        legajos (list): lista de legajos.
        cantidad (int): cantidad de posiciones ya cargadas. Al cargar el
                        estudiante i, se pasa i.

    Retorna:
        bool: True si el legajo ya existe entre los cargados, False si es
              nuevo.
    '''
    repetido = False
    i = 0
    while i < cantidad and not repetido:
        if legajos[i] == legajo:
            repetido = True
        i += 1
    return repetido


def validar_nombre(dato: str) -> bool:
    '''
    Valida que el texto contenga solo letras (A-Z, a-z) y espacios, con al
    menos una letra. Usa una bandera y el código ASCII de cada carácter
    (A-Z = 65-90, a-z = 97-122, espacio = 32).

    Parámetros:
        dato (str): nombre y apellido ingresados.

    Retorna:
        bool: True si todos los caracteres son letras o espacios y hay al
              menos una letra; False si hay otro carácter o solo espacios.
    '''
    hay_letra = False
    for caracter in dato:
        codigo = ord(caracter)
        if 65 <= codigo <= 90 or 97 <= codigo <= 122:
            hay_letra = True
        elif codigo != 32:
            return False
    return hay_letra


def validar_genero(dato: str) -> bool:
    '''
    Valida que el género sea 'F', 'M' o 'X'.

    Parámetros:
        dato (str): texto ingresado por el usuario.

    Retorna:
        bool: True si es exactamente "F", "M" o "X"; False en otro caso.
    '''
    return dato == "F" or dato == "M" or dato == "X" or dato == "f" or dato == "m" or dato == "x"


def validar_nota(dato: str) -> bool:
    '''
    Valida que el dato sea una calificación: un entero entre 1 y 10.

    Parámetros:
        dato (str): texto ingresado por el usuario.

    Retorna:
        bool: True si es numérico y está entre 1 y 10 (inclusive).

    '''
    return solo_digitos_numerico(dato) and 1 <= int(dato) <= 10


def validar_materia(dato: str, cantidad: int) -> bool:
    '''
    Valida que el dato sea un número de materia existente.

    Parámetros:
        dato (str): texto ingresado por el usuario.
        cantidad (int): cantidad total de materias (columnas de la matriz).

    Retorna:
        bool: True si es numérico y está entre 1 y 'cantidad' (inclusive).
    '''
    return solo_digitos_numerico(dato) and 1 <= int(dato) <= cantidad

#PEDIR DATOS

def pedir_legajo() -> int:
    '''
    Pide un legajo por consola y lo vuelve a pedir hasta que sea válido
    (entero de cinco cifras).

    Retorna:
        int: legajo validado, convertido a entero.
    '''
    dato = input("Legajo (5 cifras): ")
    while not validar_legajo(dato):
        print("Error: el legajo debe ser un entero de cinco cifras.")
        dato = input("Legajo (5 cifras): ")
    return int(dato)


def pedir_legajo_nuevo(legajos: list, cantidad: int) -> int:
    '''
    Pide un legajo válido (5 cifras) que además NO esté repetido entre los
    ya cargados.

    Parámetros:
        legajos (list): lista de legajos.
        cantidad (int): cantidad de posiciones ya cargadas.

    Retorna:
        int: legajo válido y no repetido.
    '''
    legajo = pedir_legajo()
    while legajo_repetido(legajo, legajos, cantidad):
        print("Error: ese legajo ya fue cargado, ingrese otro.")
        legajo = pedir_legajo()
    return legajo


def pedir_nombre() -> str:
    '''
    Pide nombre y apellido por consola y los vuelve a pedir hasta que
    contengan solo letras y espacios.

    Retorna:
        str: nombre y apellido validados.
    '''
    dato = input("Nombre y apellido: ")
    while not validar_nombre(dato):
        print("Error: solo se permiten letras y espacios.")
        dato = input("Nombre y apellido: ")
    return dato


def pedir_genero() -> str:
    '''
    Pide el género por consola y lo vuelve a pedir hasta que sea F, M o X
    (se acepta en mayúscula o minúscula). Siempre lo retorna en mayúscula.

    Retorna:
        str: género validado ("F", "M" o "X").
    '''
    dato = input("Género (F/M/X): ")
    while not validar_genero(dato):
        print("Error: ingrese F, M o X.")
        dato = input("Género (F/M/X): ")
    return dato.upper()


def pedir_nota(mensaje:str) -> int:
    '''
    Pide una calificación por consola y la vuelve a pedir hasta que sea un
    entero entre 1 y 10.

    Parámetros:
        mensaje (str): texto que se muestra al pedir la nota
                       (por ejemplo, "Nota de MATERIA_1: ").

    Retorna:
        int: nota validada, convertida a entero.
    '''
    dato = input(mensaje)
    while not validar_nota(dato):
        print("Error: ingrese un entero entre 1 y 10.")
        dato = input(mensaje)
    return int(dato)


def pedir_materia(materias: list) -> int:
    '''
    Muestra las materias numeradas y pide el número de una de ellas,
    repitiendo hasta que esté entre 1 y la cantidad de materias.

    Parámetros:
        materias (list): nombres de las materias.

    Retorna:
        int: número de materia elegido (índice de columna + 1)
    '''
    cantidad = len(materias)
    print("\nMaterias disponibles:")
    for i in range(cantidad):
        print(f"{i + 1} - {materias[i]}")
    dato = input(f"Número de materia (1 a {cantidad}): ")
    while not validar_materia(dato, cantidad):
        print(f"Error: ingrese un entero entre 1 y {cantidad}.")
        dato = input(f"Número de materia (1 a {cantidad}): ")
    return int(dato)

def pedir_opcion() -> int:
    '''
    Pide la opción del menú. Evita que el programa se rompa si el usuario
    escribe texto en lugar de un número.

    Retorna:
        int: la opción ingresada, o -1 si no es numérica. El valor -1 no
             coincide con ningún caso del menú y cae en el "case _".
    '''
    dato = input("Elija una opción: ")
    if solo_digitos_numerico(dato):
        return int(dato)
    return -1

#CARGAR DATOS

def cargar_datos(matriz: list, legajos: list, nombres: list, generos: list,
                 materias: list) -> None:
    '''
    Carga secuencial de todos los estudiantes. Para cada posición i pide
    legajo, nombre, género y una nota por cada materia (columna), validando
    cada dato. Al pedir cada nota muestra el nombre de la materia. El legajo
    no puede repetirse: se controla contra los i legajos cargados hasta el
    momento. Modifica las estructuras recibidas.

    Parámetros:
        matriz (list): matriz de calificaciones ya creada (filas x materias).
        legajos (list): lista de legajos ya creada.
        nombres (list): lista de nombres ya creada.
        generos (list): lista de géneros ya creada.
        materias (list): nombres de las materias; materias[j] corresponde a la columna j.
    '''
    for i in range(len(legajos)):
        print(f"\n--- Estudiante {i + 1} de {len(legajos)} ---")
        legajos[i] = pedir_legajo_nuevo(legajos, i)
        nombres[i] = pedir_nombre()
        generos[i] = pedir_genero()
        for j in range(len(matriz[i])):
            matriz[i][j] = pedir_nota(f"Nota de {materias[j]}: ")
    print("\nDatos cargados correctamente.")


#MOSTRAR DATOS

def mostrar_encabezado(materias: list, con_promedio: bool = False) -> None:
    '''
    Muestra la fila de títulos de la tabla, con una columna por materia
    (usando el nombre de cada una) y una línea separadora.

    Parámetros:
        materias (list): nombres de las materias, uno por columna.
        con_promedio (bool): si es True agrega la columna PROMEDIO. Por defecto es False.

    '''
    linea = f"{'LEGAJO':<8}{'NOMBRE':<25}{'SEXO':<6}"
    for j in range(len(materias)):
        linea += f"{materias[j]:<12}"
    if con_promedio:
        linea += "PROMEDIO"
    print(linea)
    print("-" * len(linea))


def mostrar_estudiante(i: int, matriz: list, legajos: list, nombres: list,
                       generos: list, promedios: list = None) -> None:
    '''
    Muestra los datos de un solo estudiante: legajo, nombre, género y sus
    notas.

    Parámetros:
        i (int): posición del estudiante (índice de fila).
        matriz (list): matriz de calificaciones.
        legajos (list): lista de legajos.
        nombres (list): lista de nombres.
        generos (list): lista de géneros.
        promedios (list): lista de promedios. Opcional: si se omite, no se muestra la columna de promedio.
    '''
    linea = f"{legajos[i]:<8}{nombres[i]:<25}{generos[i]:<6}"
    for j in range(len(matriz[i])):
        linea += f"{matriz[i][j]:<12}"
    if promedios is not None:
        linea += f"{promedios[i]:.2f}"
    print(linea)


def mostrar_estudiantes(matriz: list, legajos: list, nombres: list,
                        generos: list, materias: list, promedios: list = None) -> None:
    '''
    Muestra todos los estudiantes en forma de tabla: imprime el encabezado y
    recorre las filas llamando a mostrar_estudiante para cada una.

    Parámetros:
        matriz (list): matriz de calificaciones.
        legajos (list): lista de legajos.
        nombres (list): lista de nombres.
        generos (list): lista de géneros.
        materias (list): nombres de las materias (para el encabezado).
        promedios (list): lista de promedios. Opcional: si se pasa, se agrega la columna PROMEDIO.
    '''
    mostrar_encabezado(materias, promedios is not None)
    for i in range(len(legajos)):
        mostrar_estudiante(i, matriz, legajos, nombres, generos, promedios)

def mostrar_materia(nombre: str, promedio: float) -> None:
    '''
    Muestra UNA materia con su nombre y su promedio con dos decimales.
    Es la función "mostrar una".

    Parámetros:
        nombre (str): nombre de la materia (por ejemplo, "Literatura").
        promedio (float): promedio general de esa materia.
    '''
    print(f"{nombre} - Promedio general: {promedio:.2f}")
    
#PROMEDIOS ESTUDIANTE

def calcular_promedio(fila: list) -> float:
    '''
    Calcula el promedio de una lista de notas (una fila de la matriz):
    acumula la suma de las notas y la divide por la cantidad de notas.
    No redondea; el formato de dos decimales se aplica al mostrar.

    Parámetros:
        fila (list): notas de UN estudiante (una fila de la matriz).

    Retorna:
        float: promedio de las notas.
    '''
    suma = 0
    for nota in fila:
        suma += nota
    return suma / len(fila)


def calcular_promedios(matriz: list, promedios: list) -> None:
    '''
    Calcula el promedio de cada estudiante y lo guarda en la lista 'promedios', en la misma posición del estudiante.

    Parámetros:
        matriz (list): matriz de calificaciones.
        promedios (list): lista ya creada, de igual tamaño que la cantidad
                          de filas, donde se guardan los resultados.

    Retorna:
        None
    '''
    for i in range(len(matriz)):
        promedios[i] = calcular_promedio(matriz[i])

#ORDENAMIENTO

def intercambiar_estudiantes(a: int, b: int, matriz: list, legajos: list,
                             nombres: list, generos: list, promedios: list) -> None:
    '''
    Intercambia las posiciones 'a' y 'b' en TODAS las estructuras paralelas,
    incluida la fila completa de la matriz, para que cada estudiante siga
    correspondiéndose con sus propios datos y notas.

    Parámetros:
        a (int): posición de un estudiante.
        b (int): posición del otro estudiante.
        matriz, legajos, nombres, generos, promedios (list): estructuras
            paralelas que se modifican.

    Retorna:
        None
    '''
    matriz[a], matriz[b] = matriz[b], matriz[a]
    legajos[a], legajos[b] = legajos[b], legajos[a]
    nombres[a], nombres[b] = nombres[b], nombres[a]
    generos[a], generos[b] = generos[b], generos[a]
    promedios[a], promedios[b] = promedios[b], promedios[a]


def ordenar_estudiantes(matriz: list, legajos: list, nombres: list,
                        generos: list, promedios: list, orden: str) -> None:
    '''
    Ordena a los estudiantes por promedio usando el método de burbuja.

    Parámetros:
        matriz, legajos, nombres, generos, promedios (list): estructuras
            paralelas que se modifican.
        orden (str): "ASC" para ascendente (menor a mayor); cualquier otro
                     valor, por ejemplo "DESC", ordena descendente.

    Retorna:
        None
    '''
    n = len(promedios)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if orden == "ASC":
                cambiar = promedios[j] > promedios[j + 1]
            else:
                cambiar = promedios[j] < promedios[j + 1]
            if cambiar:
                intercambiar_estudiantes(j, j + 1, matriz, legajos, nombres,
                                         generos, promedios)

#PROMEDIOS POR MATERIA

def promedio_materia(matriz: list, columna: int) -> float:
    '''
    Calcula el promedio general de una materia. Recorre una columna: la
    columna queda fija y varía la fila.

    Parámetros:
        matriz (list): matriz de calificaciones.
        columna (int): índice de la columna (materia), empezando en 0.

    Retorna:
        float: promedio de todas las notas de esa materia.
    '''
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]
    return suma / len(matriz)


def calcular_promedios_materias(matriz: list) -> list:
    '''
    Calcula el promedio general de cada materia (cada columna).

    Parámetros:
        matriz (list): matriz de calificaciones.

    Retorna:
        list: lista de floats con un promedio por materia. La posición j corresponde a la materia materias[j] (columna j).
    '''
    promedios = crear_lista(len(matriz[0]), 0.0)
    for j in range(len(matriz[0])):
        promedios[j] = promedio_materia(matriz, j)
    
    return promedios


def mostrar_materias_mayor_promedio(matriz: list, materias: list) -> None:
    '''
    Muestra TODAS las materias con el mayor promedio general (puede haber
    empate). Calcula los promedios, busca el máximo y luego muestra, con
    mostrar_materia, cada materia cuyo promedio lo iguala.

    Parámetros:
        matriz (list): matriz de calificaciones.
        materias (list): nombres de las materias; materias[j] corresponde a la columna j.

    Retorna:
        None
    '''
    promedios = calcular_promedios_materias(matriz)
    mayor = promedios[0]
    for j in range(len(promedios)):
        if promedios[j] > mayor:
            mayor = promedios[j]

    print("\nMateria/s con mayor promedio general:")
    for j in range(len(promedios)):
        if promedios[j] == mayor:
            mostrar_materia(materias[j], promedios[j])

#BUSQUEDA DE LEGAJO

def buscar_legajo(legajo: int, legajos: list) -> int:
    '''
    Búsqueda secuencial de un legajo. Corta apenas lo encuentra. 
    Si no lo encuentra, retorna -1.

    Parámetros:
        legajo (int): legajo a buscar.
        legajos (list): lista de legajos donde se busca.

    Retorna:
        int: posición donde está el legajo, o -1 si no existe.
    '''
    posicion = -1
    
    i = 0
    
    while i < len(legajos) and posicion == -1:
        if legajos[i] == legajo:
            posicion = i
        i += 1
    
    return posicion

def buscar_por_legajo(matriz: list, legajos: list, nombres: list,
                      generos: list, materias: list, promedios: list) -> None:
    '''
    Pide un legajo, lo busca con buscar_legajo y muestra todos los datos del
    estudiante. Si el legajo no existe, lo informa.

    Parámetros:
    matriz, legajos, nombres, generos (list): estructuras paralelas.
    materias (list): nombres de las materias (para el encabezado).
    promedios (list): promedios ya calculados (ítem 3).
    '''
    legajo = pedir_legajo()
    posicion = buscar_legajo(legajo, legajos)
    if posicion != -1:
        print("\nEstudiante encontrado:")
        mostrar_encabezado(materias, True)
        mostrar_estudiante(posicion, matriz, legajos, nombres, generos, promedios)
    else:
        print(f"No se encontró ningún estudiante con el legajo {legajo}.")

#REPETICION

def contar_calificaciones(matriz: list, materia: int) -> list:
    '''
    Cuenta cuántas veces aparece cada nota (1 a 10) en una materia.

    Parámetros:
        matriz (list): matriz de calificaciones.
        materia (int): número de materia (índice de columna + 1).

    Retorna:
        list: lista de 10 enteros. En el índice 0 está la cantidad de veces
              que aparece la nota 1, en el índice 1 la de la nota 2, y así
              hasta el índice 9, que corresponde a la nota 10.
    '''
    repeticion = crear_lista(10)
    columna = materia - 1
    for i in range(len(matriz)):
        nota = matriz[i][columna]
        repeticion[nota - 1] += 1
    return repeticion


def mostrar_frecuencias(matriz: list, materias: list) -> None:
    '''
    Muestra las materias, pide una, calcula con contar_calificaciones
    cuántas veces se repite cada nota y muestra el resultado con el nombre
    de la materia elegida.

    Parámetros:
        matriz (list): matriz de calificaciones.
        materias (list): nombres de las materias.

    '''
    materia = pedir_materia(materias)
    repeticion = contar_calificaciones(matriz, materia)
    print(f"\nFrecuencia de notas en {materias[materia - 1]}:")
    for i in range(len(repeticion)):
        print(f"Nota {i + 1}: {repeticion[i]} vez/veces")