#ejercio A
'''
for i in range(1, 11):
    print(i)
    
#Ejercicio B

for i in range(10, 0, -1):
    print(i)
    
#Ejercicio C

numero = int(input("ingrese un numero: "))

for i in range(0, numero):
    print("Hola UTN FRA")
    
#Ejercicio D

numero = int(input("Ingrese un numero: "))

for i in range(numero):
    if i % 2 == 0:
        print(i)
      
#Ejercicio E

numero = int(input("Ingrese un numero: "))

for i in range(0, numero):
    if i % 2 != 0:
        print(i)
        
#Ejercicio F

#for i in range(1, 10):
for _ in iter(int,1):
    numero = int(input("Ingresa un numero (mayor a 0): "))
    if numero > 0:
        print(numero)
    else:
        break
        
        '''

numero = int(input("Ingrese un numero: "))        
divisible = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisible += 1
        
if divisible == 2:
    print("Es primo")
else:
    print("No es primo")