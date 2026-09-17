#Ejercicio D
'''
letra = input("Ingresa una letra: ")

while True:
    if letra == "F" and letra == "f":
        print("FEMENINO")
        break
    elif letra == "M" and letra == "m":
        print("MASCULINO")
        break
    else:
        letra = input("Ingresa una letra: ")
       '''
        
#Ejercicio G

multiplicacion = 1
suma = 0
continuar = 'S'
bandera = False
while continuar == 'S' or continuar == 's':
    numero = int(input("NUMERO: "))
    if numero > 0:
        suma += numero
    else:
        multiplicacion *= numero
        bandera = True
        
    continuar = input("Desea ingresar otro numero? [S|N]")

if bandera == False:
    multiplicacion = 0    

print(f"La suma es: {suma}, la multiplicacion de los numero negativos es: {multiplicacion}")




