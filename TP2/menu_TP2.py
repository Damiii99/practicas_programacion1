from funciones_TP2 import (
    mostrar_menu,
    pedir_opcion_menu,
    acceso_permitido,
    opcion_cargar_datos,
    opcion_mostrar_datos,
    opcion_calcular_promedios,
    opcion_ordenar_por_promedio,
    opcion_materia_mayor_promedio,
    opcion_buscar_por_legajo,
    opcion_contar_notas,
)


def menu() -> None:
    
    estudiantes = []   

    while True:
        mostrar_menu()
        opcion = pedir_opcion_menu()

    
        if not acceso_permitido(opcion, estudiantes):
            continue

        match opcion:
            case 1:
                opcion_cargar_datos(estudiantes)
            case 2:
                opcion_mostrar_datos(estudiantes)
            case 3:
                opcion_calcular_promedios(estudiantes)
            case 4:
                opcion_ordenar_por_promedio(estudiantes)
            case 5:
                opcion_materia_mayor_promedio(estudiantes)
            case 6:
                opcion_buscar_por_legajo(estudiantes)
            case 7:
                opcion_contar_notas(estudiantes)
            case 8:
                print("Saliendo del programa...")
                break


if __name__ == "__main__":
    menu()

    
