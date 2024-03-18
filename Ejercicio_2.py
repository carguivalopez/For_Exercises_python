''' 
Crea dos arrays o arreglo unidimensional es que tengan el mismo tamaño (lo pedirá por teclado), 
en uno de ellos almacenarás nombres de personas como cadenas, en el otro array o arreglo ira almacenando la edad de las 
personas. Mostrar las personas y edades.
'''

# Ejercicio 2


A = int(input("Ingrese el tamaño de los arreglos: "))
B = []
C = []

# Solicitar nombres y edades
for i in range(A):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))
    edad = int(input("Ingrese la edad de la persona {}: ".format(i + 1)))
    B.append(nombre)
    C.append(edad)

# Mostrar nombres y edades
print("Nombres de las personas:")
for nombre in B:
    print(nombre)

print("\nEdades de las personas:")
for edad in C:
    print(edad)
