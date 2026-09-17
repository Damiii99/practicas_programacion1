#Ejercicio if/elif/else
'''
#A) Al ingresar un número por input, evaluar si el mismo es 1980, si es así mostrar el mensaje "Este año se creó del videojuego Pac-Man" por consola.

fecha = 1980
numero = int(input("ingrese un numero: "))

if numero == fecha:
    print("Este año se creó del videojuego Pac-Man")

#B) Al ingresar una edad por input se debe informar por consola si la persona es mayor de edad, caso contrario no informar nada. 

edad = input("Ingrese tu edad: ")

if edad >= 18:
    print("Es mayor de edad")


#C) Al ingresar una edad por input se debe informar si la persona es mayor de edad, caso contrario, informar que es un menor de edad

edad = input("Ingrese tu edad: ")

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#D)  Al ingresar una edad por input, se debe informar si la persona es adolescente, edad entre 13 y 17 años (inclusive), caso contrario, no informar nada.

edad = int(input("Ingrese la edad: "))

if 13 <= edad <= 17:
    print("La persona es adolescente")
'''
#E) Al ingresar una edad por input, solo se debe informar si la persona NO es adolescente.

edad = int(input("Ingrese edad: "))

if not edad < 18 and not edad > 12:
    print("No es adolescente")
    
#F)  Al ingresar una edad por input, se debe informar si la persona es mayor de edad (mayor a 17 años) o adolescente (entre 13 y 17 años) o niño (menor a 13 años). 
'''
edad = int(input("Ingrese una eda: "))

if edad > 17:
    print("Es mayor de edad")
elif edad < 13:
    print("Es niño")
else:
    print("Es adolencete")
    
    '''