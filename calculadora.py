'''
Calculadora con sus cuatro operaciones basicas
'''
def sumar(numero_a: float, numero_b: float) ->float:
    resultado = numero_a + numero_b
    return resultado
    
def restar(numero_a: float, numero_b: float) ->float:
    resultado = numero_a - numero_b
    return resultado

def multiplicar(numero_a, numero_b):
    resultado = numero_a * numero_b
    return resultado
    
def dividir(numero_a: float, numero_b: float)->float:
    retorno = None
    if numero_b != 0:
        resultado = numero_a / numero_b
        retorno = resultado
    return retorno

def div(numero_a: float, numero_b: float)->float:
    resultado = numero_a / numero_b
    return resultado
        

nro_1 = float(input("Primer operando: "))
nro_2 = float(input("Segundo operando: "))



while True:
    print("1-SUMAR\n2-RESTAR\n3-MULTIPLICAR\n4-DIVIDIR\n5-SALIR")
    opciones = int(input("Elije una opcion: "))

    match opciones:
        case 1:
            resultado = sumar(nro_1, nro_2)
            print(f"La suma es: {resultado}")
        case 2:
            resultado = restar(nro_1, nro_2)
            print(f"La resta es: {resultado}")
        case 3:
            resultado = multiplicar(nro_1, nro_2)
            print(f"La multiplicacion es: {resultado}")
        case 4:
            resultado = dividir(nro_1, nro_2)
            if resultado != None:
                print(f"La division es: {resultado}")
            else:
                print("ERROR, no se puede dividir por cero")
        case 5:
            print("Cerrando Programa")
            break
        case _:
            print("!ERROR¡ opcion no encontrada")