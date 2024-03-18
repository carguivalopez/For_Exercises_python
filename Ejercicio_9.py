''' 
Ejercicio 9
Hacer un programa que inicialice un vector de números con valores aleatorios, y posterior ordene los elementos de menor a mayor.
'''

#Ejercicio 9 

import random

# Inicializar un vector de números con valores aleatorios
vector = [random.randint(1, 100) for _ in range(10)]

print("Vector inicial:", vector)

# Ordenar los elementos de menor a mayor
vector.sort()

print("Vector ordenado de menor a mayor:", vector)
