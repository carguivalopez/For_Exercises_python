''' 
Ejercicio 5
Realizar un programa que defina un arreglo llamado “arreglo_numeros” de 10 enteros, a continuación, lo inicialice 
con valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento del arreglo junto con su cuadrado y su cubo.
'''

#Ejercicio 5


import random

# Definir el arreglo de 10 enteros
arreglo_numeros = []

# Inicializar el arreglo con valores aleatorios del 1 al 10
for _ in range(10):
    arreglo_numeros.append(random.randint(1, 10))

# Mostrar cada elemento del arreglo junto con su cuadrado y su cubo
print("Elementos del arreglo junto con su cuadrado y su cubo:")
for num in arreglo_numeros:
    cuadrado = num ** 2
    cubo = num ** 3
    print("Número:", num, "- Cuadrado:", cuadrado, "- Cubo:", cubo)

