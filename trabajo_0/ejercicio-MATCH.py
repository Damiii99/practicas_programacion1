'''
#Ejercicio A.

mes = input("Ingrese un mes: ")

match mes:
    case "enero":
        print("Que comiences bien el año")
    case "marzo":
        print("A clases")
    case "julio":
        print("Se vienen las vacaciones")
    case "diciembre":
        print("Felices fiesta")
    case _:
        print("Opcion invalida")
#Ejercicio B.

mes = input("Ingrese un mes: ")

match mes:
    case "enero":
        print("Falta para el invierno.")
    case "febrero":
        print("Falta para el invierno.")
    case "marzo":
        print("Falta para el invierno.")
    case "abril":
        print("Falta para el invierno.")
    case "mayo":
        print("Falta para el invierno.")
    case "junio":
        print("Falta para el invierno.")
    case "julio":
        print("Abrigate que hace frio.")
    case "agosto":
        print("Abrigate que hace frio.")
    case "septiembre":
        print("Ya pasamos el frio, ahora calor!")
    case "octubre":
        print("Ya pasamos el frio, ahora calor!")
    case "noviembre":
        print("Ya pasamos el frio, ahora calor!")
    case "diciembre":
        print("Ya pasamos el frio, ahora calor!")
    case _:
            print("Opcion invalida")


#Ejercicio C

mes = input("Ingrese un mes: ")

match mes:
    case "febrero":
        print("Este mes no tiene mas de 29 días")
    case "enero" | "marzo" | "mayo" | "abril" | "junio" | "julio" | "septiembre" | " noviembre" | "agosto" | "octubre" | "diciembre":
        print("Este mes tiene 30 o más días")
    case _:
        print("mes no valido")

#Ejercico D

mes = input("Ingrese un mes: ")

match mes:
    case "enero" | "marzo" | "mayo" | "julio" | "agosto" | "octubre" | "diciembre":
        print("tiene 31 dias")
    case "abril" | "junio" | "septiembre" | " noviembre":
        print("tiene 30 dias")
    case "febrero":
        print("Tiene 28 dias")
    case _:
        print("mes no valido")    
        
        
#Ejercicio E

numero = int(input("Ingrese un numero: "))

match numero:
    case hora if 7 <= hora <= 11:
            print("Es de mañana")
     '''       
#Ejercicio G

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un numero: "))

opciones = input("Elige una opcion \nsumar\nrestar\nmultiplicar\ndividir ")

match opciones:
    case "sumar":
        print(f"El resultado es {numero_1 + numero_2}")
    case "restar":
        print(f"El resultado es {numero_1 - numero_2}")
    case "multiplicar":
        print(f"El resultado es {numero_1 * numero_2}")
    case "dividir":
        if numero_2 == 0:
            print("El denominador no puede ser 0")
        else:    
            print(f"El resultado es {numero_1 / numero_2}")
    case _:
        print("opcion invalida")