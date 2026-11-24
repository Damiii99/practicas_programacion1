from funciones_TP4 import (
    CANTIDAD_NOTAS,
    pedir_entero_en_rango,
    pedir_legajo,
    pedir_orden,
    cargar_desde_csv,
    cargar_manual,
    normalizar_estudiantes,
    calcular_promedios,
    ordenar_por_promedio,
    mostrar_menores_a_cuatro,
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


def opcion_normalizar(estudiantes: list) -> None:
    """
    Ítem 3: normaliza y convierte a mayúsculas los datos str (paradigma funcional).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    normalizar_estudiantes(estudiantes)
    print(f"\nDatos de texto normalizados a mayúsculas en {len(estudiantes)} estudiantes.")


def opcion_mostrar_datos(estudiantes: list) -> None:
    """
    Ítem 4: muestra la lista completa de estudiantes con su encabezado.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print("\n--- LISTA DE ESTUDIANTES ---")
    mostrar_estudiantes(estudiantes)


def opcion_calcular_promedios(estudiantes: list) -> None:
    """
    Ítem 5: calcula y guarda el promedio de cada estudiante (lambda + map).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    calcular_promedios(estudiantes)
    print(f"\nPromedios calculados y guardados para {len(estudiantes)} estudiantes.")


def opcion_ordenar_por_promedio(estudiantes: list) -> None:
    """
    Ítem 6: pide el orden (ASC o DESC), ordena por promedio y muestra el resultado.

    Args:
        estudiantes (list): lista de diccionarios (se ordena en el lugar).

    Returns:
        None.
    """
    print("\n--- ORDENAR POR PROMEDIO ---")
    orden = pedir_orden()
    ordenar_por_promedio(estudiantes, orden)
    print()
    mostrar_estudiantes(estudiantes)


def opcion_filtrar_menores_a_cuatro(estudiantes: list) -> None:
    """
    Ítem 7: filtra y muestra los estudiantes con promedio menor a 4 (filter).

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print("\n--- ESTUDIANTES CON PROMEDIO MENOR A 4 ---")
    mostrar_menores_a_cuatro(estudiantes)


def opcion_materia_mayor_promedio(estudiantes: list) -> None:
    """
    Ítem 8: muestra la/s materia/s con mayor promedio general.

    Args:
        estudiantes (list): lista de diccionarios de estudiantes.

    Returns:
        None.
    """
    print()
    mostrar_materias_mayor_promedio(estudiantes)


def opcion_buscar_por_legajo(estudiantes: list) -> None:
    """
    Ítem 9: busca un estudiante por legajo y muestra todos sus datos
    (incluido el promedio calculado en el ítem 5).

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
    Ítem 10: pide una materia y muestra cuántas veces se repite cada nota (1 a 10).

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
    Ítem 11: pide el nombre del archivo y guarda la lista completa en formato JSON.

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
    elige la opción 12. En cada vuelta se muestra el menú, se pide la opción
    (validada entre 1 y 12) y un match llama a la función del ítem elegido.

    Control de acceso (Nota 1):
        - datos_cargados: bandera que indica si ya hay estudiantes en la lista.
          Se actualiza con hay_datos() después de cargar (opciones 1 y 2), así
          que si una carga falla la bandera sigue en False.
        - Opciones 3 a 11: requieren datos cargados.
        - Opciones 6 y 9: además requieren promedios calculados (opción 5).
        - La opción 7 (filter) controla los promedios dentro de su propia función.

    Returns:
        None.
    """
    estudiantes = []        
    datos_cargados = False

    while True:
        print(" ")
        print("\t MENÚ DE DATOS DE ESTUDIANTES")
        print(" 1. Cargar los datos desde un archivo CSV")
        print(" 2. Cargar los datos manualmente")
        print(" 3. Normalizar los datos de texto a mayúsculas")
        print(" 4. Mostrar todos los datos")
        print(" 5. Calcular el promedio de cada estudiante")
        print(" 6. Ordenar y mostrar por promedio")
        print(" 7. Mostrar los estudiantes con promedio menor a 4")
        print(" 8. Mostrar la/s materia/s con mayor promedio general")
        print(" 9. Buscar un estudiante por legajo")
        print("10. Contar cuántas veces se repite cada nota en una materia")
        print("11. Guardar los datos en un archivo JSON")
        print("12. Salir del programa")
        print(" ")

        opcion = pedir_entero_en_rango("Elegí una opción: ", 1, 12)

        if opcion in (3, 4, 5, 6, 7, 8, 9, 10, 11) and not datos_cargados:
            print("\nERROR: primero tenés que cargar los datos (opción 1 o 2).")
        elif opcion in (6, 9) and not promedios_calculados(estudiantes):
            print("\nERROR: primero tenés que calcular los promedios (opción 5).")
        else:
            match opcion:
                case 1:
                    opcion_cargar_csv(estudiantes)
                    datos_cargados = hay_datos(estudiantes)
                case 2:
                    opcion_cargar_manual(estudiantes)
                    datos_cargados = hay_datos(estudiantes)
                case 3:
                    opcion_normalizar(estudiantes)
                case 4:
                    opcion_mostrar_datos(estudiantes)
                case 5:
                    opcion_calcular_promedios(estudiantes)
                case 6:
                    opcion_ordenar_por_promedio(estudiantes)
                case 7:
                    opcion_filtrar_menores_a_cuatro(estudiantes)
                case 8:
                    opcion_materia_mayor_promedio(estudiantes)
                case 9:
                    opcion_buscar_por_legajo(estudiantes)
                case 10:
                    opcion_contar_notas(estudiantes)
                case 11:
                    opcion_guardar_json(estudiantes)
                case 12:
                    print("Saliendo del programa...")
                    break


if __name__ == "__main__":
    menu()