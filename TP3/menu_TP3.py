
from funciones_TP3 import (
    CANTIDAD_NOTAS,
    pedir_entero_en_rango,
    pedir_legajo,
    pedir_orden,
    cargar_desde_csv,
    cargar_manual,
    calcular_promedios,
    ordenar_por_promedio,
    contar_notas,
    buscar_estudiante,
    hay_datos,
    promedios_calculados,
    mostrar_encabezado,
    mostrar_estudiante,
    mostrar_estudiantes,
    mostrar_materias_mayor_promedio,
    mostrar_conteo_notas,
    guardar_json,
)

def opcion_cargar_csv(estudiantes: list) -> None:
    """
    Ítem 1: pide por consola el nombre del archivo CSV y carga los datos.

    Args:
        estudiantes (list): lista de diccionarios que se va a completar.

    Returns:
        None.
    """
    print("\n--- CARGA DESDE CSV ---")
    ruta = input("Nombre del archivo CSV (ej: estudiantes.csv): ").strip()
    cargar_desde_csv(estudiantes, ruta)


def opcion_cargar_manual(estudiantes: list) -> None:
    """
    Ítem 2: carga manual de estudiantes con validación de cada dato.

    Args:
        estudiantes (list): lista de diccionarios a la que se agregan los nuevos.

    Returns:
        None.
    """
    print("\n--- CARGA MANUAL ---")
    cargar_manual(estudiantes)


def opcion_mostrar_datos(estudiantes: list) -> None:
    """
    Ítem 3: muestra la lista completa de estudiantes con su encabezado.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print("\n--- LISTA DE ESTUDIANTES ---")
    mostrar_estudiantes(estudiantes)


def opcion_calcular_promedios(estudiantes: list) -> None:
    """
    Ítem 4: calcula y guarda el promedio de cada estudiante.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    calcular_promedios(estudiantes)
    print(f"\nPromedios calculados y guardados para {len(estudiantes)} estudiantes.")


def opcion_ordenar_por_promedio(estudiantes: list) -> None:
    """
    Ítem 5: pide el orden (ASC o DESC), ordena por promedio y muestra el resultado.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes (se ordena en el lugar).

    Returns:
        None.
    """
    print("\n--- ORDENAR POR PROMEDIO ---")
    orden = pedir_orden()
    ordenar_por_promedio(estudiantes, orden)
    print()
    mostrar_estudiantes(estudiantes)


def opcion_materia_mayor_promedio(estudiantes: list) -> None:
    """
    Ítem 6: muestra la/s materia/s con mayor promedio general.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print()
    mostrar_materias_mayor_promedio(estudiantes)


def opcion_buscar_por_legajo(estudiantes: list) -> None:
    """
    Ítem 7: busca un estudiante por legajo y muestra todos sus datos
    (incluido el promedio calculado en el ítem 4).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
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
    Ítem 8: pide una materia y muestra cuántas veces se repite cada nota (1 a 10).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print("\n--- REPETICIÓN DE NOTAS POR MATERIA ---")
    numero = pedir_entero_en_rango(f"Materia (1 a {CANTIDAD_NOTAS}): ", 1, CANTIDAD_NOTAS)
    indice = numero - 1                      # MAT_1 -> índice 0
    conteo = contar_notas(estudiantes, indice)
    mostrar_conteo_notas(conteo, indice)


def opcion_guardar_json(estudiantes: list) -> None:
    """
    Ítem 9: pide el nombre del archivo y guarda la lista completa en formato JSON.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print("\n--- GUARDAR EN JSON ---")
    ruta = input("Nombre del archivo JSON (ej: estudiantes.json): ").strip()
    if guardar_json(estudiantes, ruta):
        print(f"Se guardaron {len(estudiantes)} estudiantes en '{ruta}'.")
    else:
        print(f"ERROR: no se pudo guardar el archivo '{ruta}'.")


def menu() -> None:
    """
    Ejecuta el menú principal del programa.

    El menú está anidado dentro de un while que se repite hasta que el usuario
    elige la opción 10. En cada vuelta se muestra el menú, se pide la opción
    (validada entre 1 y 10) y un match llama a la función del ítem elegido.

    Control de acceso (Nota 1):
        - datos_cargados: bandera que indica si ya hay estudiantes en la lista.
          Se actualiza después de cargar (opciones 1 y 2) con hay_datos(), así
          que si una carga falla (ej: archivo inexistente) la bandera sigue en
          False y no se habilitan los demás ítems.
        - Opciones 3 a 9: requieren datos cargados.
        - Opciones 5 y 7: además requieren promedios calculados (opción 4),
          porque ordenan por promedio y muestran el promedio del estudiante.

    La lista 'estudiantes' se crea acá y se pasa a cada función, así todas
    trabajan sobre los mismos datos.

    Returns:
        None.
    """
    estudiantes = []            # lista de diccionarios: acá se guarda todo
    datos_cargados = False

    while True:
        print(" ")
        print("\t MENÚ DE DATOS DE ESTUDIANTES")
        print(" 1. Cargar los datos desde un archivo CSV")
        print(" 2. Cargar los datos manualmente")
        print(" 3. Mostrar todos los datos")
        print(" 4. Calcular el promedio de cada estudiante")
        print(" 5. Ordenar y mostrar por promedio")
        print(" 6. Mostrar la/s materia/s con mayor promedio general")
        print(" 7. Buscar un estudiante por legajo")
        print(" 8. Contar cuántas veces se repite cada nota en una materia")
        print(" 9. Guardar los datos en un archivo JSON")
        print("10. Salir del programa")
        print(" ")

        opciones = pedir_entero_en_rango("Elegí una opción: ", 1, 10)

        match opciones:
            case 1:
                opcion_cargar_csv(estudiantes)
                datos_cargados = hay_datos(estudiantes)
            case 2:
                opcion_cargar_manual(estudiantes)
                datos_cargados = hay_datos(estudiantes)
            case 3:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                else:
                    opcion_mostrar_datos(estudiantes)
            case 4:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                else:
                    opcion_calcular_promedios(estudiantes)
            case 5:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                elif promedios_calculados(estudiantes) == False:
                    print("\nERROR: primero tenés que calcular los promedios (opción 4).")
                else:
                    opcion_ordenar_por_promedio(estudiantes)
            case 6:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                else:
                    opcion_materia_mayor_promedio(estudiantes)
            case 7:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                elif promedios_calculados(estudiantes) == False:
                    print("\nERROR: primero tenés que calcular los promedios (opción 4).")
                else:
                    opcion_buscar_por_legajo(estudiantes)
            case 8:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                else:
                    opcion_contar_notas(estudiantes)
            case 9:
                if datos_cargados == False:
                    print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
                else:
                    opcion_guardar_json(estudiantes)
            case 10:
                print("Saliendo del programa...")
                break
            case _:
                print("ERROR: opción no encontrada.")
