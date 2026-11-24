import funciones_TP1 as f

FILAS = 30      
MATERIAS = ["Literatura", "Matematica", "Biologia", "Historia", "Fisica"]
COLUMNAS = 5


def menu() -> None:
    datos_cargados = False
    legajos = f.crear_lista(FILAS)
    nombres = f.crear_lista(FILAS, "")
    generos = f.crear_lista(FILAS, "")
    matriz = f.crear_matriz(FILAS, COLUMNAS)
    promedios = f.crear_lista(FILAS, 0.0)

    while True:
        print("\n\t MENU DE DATOS DE ESTUDIANTES")
        print("1. Cargar datos")
        print("2. Mostrar todos los datos")
        print("3. Calcular y mostrar promedio de cada estudiante")
        print("4. Ordenar y mostrar por promedio (DESC)")
        print("5. Mostrar materia/s con mayor promedio general")
        print("6. Buscar estudiante por legajo")
        print("7. Frecuencia de calificaciones de una materia")
        print("8. Salir\n")

        opcion = f.pedir_opcion()

        if opcion in (2, 3, 4, 5, 6, 7) and not datos_cargados:
            print("ERROR: primero debe cargar los datos (opción 1).")
        else:
            match opcion:
                case 1:
                    f.cargar_datos(matriz, legajos, nombres, generos, MATERIAS)
                    datos_cargados = True
                case 2:
                    f.mostrar_estudiantes(matriz, legajos, nombres, generos, MATERIAS)
                case 3:
                    f.calcular_promedios(matriz, promedios)
                    f.mostrar_estudiantes(matriz, legajos, nombres, generos, MATERIAS, promedios)
                case 4:
                    f.calcular_promedios(matriz, promedios)
                    f.ordenar_estudiantes(matriz, legajos, nombres, generos, promedios, "DESC")
                    f.mostrar_estudiantes(matriz, legajos, nombres, generos, MATERIAS, promedios)
                case 5:
                    f.mostrar_materias_mayor_promedio(matriz, MATERIAS)
                case 6:
                    f.calcular_promedios(matriz, promedios)
                    f.buscar_por_legajo(matriz, legajos, nombres, generos, MATERIAS, promedios)
                case 7:
                    f.mostrar_frecuencias(matriz, MATERIAS)
                case 8:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("ERROR: opción no válida.")

if __name__ == "__main__":
    menu()