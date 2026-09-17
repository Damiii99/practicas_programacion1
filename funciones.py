'''
def sumar(numero_a:int, numero_b:int) -> int:
    """Funcion que se encargar de sumar dos
    números enteros
    
    Args:
        numero_a (int): Primer número
        numero_b (int): Segundo número
        
    Returns:
        int: Devuelve la suma entre estos dos 
        números
    """
    suma = numero_a + numero_b
    return suma

def restar(numero_a:int , numero_b:int)->int:
    """ Funcion que se encarga de restar dos números enteros
    Args:
        numero_a (int): Primer numero
        numero_b (int): Segundo numero

    Returns:
        int: Devuelve la resta entre estos dos numero
    """
    resta = numero_a - numero_b
    return resta

def producto(numero_a:int , numero_b:int)->int:
    """ Funcion que se encarga de multiplicar dos números enteros
    Args:
        numero_a (int): Primer numero
        numero_b (int): Segundo numero

    Returns:
        int: Devuelve la multiplicacion entre estos dos numero
    """
    multiplicacion = numero_a * numero_b
    return multiplicacion

def division(numero_a:int , numero_b:int)->int:
    """ Funcion que se encarga de dividir dos números enteros
    Args:
        numero_a (int): Primer numero
        numero_b (int): Segundo numero

    Returns:
        int: Devuelve la division entre estos dos numero
    """
    retorno = None
    if numero_b != 0:
        resultado = numero_a / numero_b
        return resultado
    else:
        print("!ERROR¡ no se puede dividir por 0")
    return retorno

num_1 = float(input("Ingrese un numero: "))
num_2 = float(input("Ingrese un segundo numero: "))

resultado_suma = sumar(num_1, num_2)
print(f"El resultado de la suma es: {resultado_suma}")

resultado_resta = restar(num_1,num_2)
print(f"El resultado de la resta es: {resultado_resta}")

resultado_producto = producto(num_1,num_2)
print(f"El resultado de la multiplicacion es: {resultado_producto}")

resultado_division = division(num_1, num_2)
print(F"El resultado de la division es: {resultado_division}")
'''

