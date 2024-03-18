''' 
Ejercicio 8
Programa que declare un vector de diez elementos enteros y pida números para rellenarlo hasta que se llene el vector o
 se introduzca un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
'''

#Ejercicio 8

# Declarar un vector de diez elementos enteros
vector = []

# Pedir números para rellenar el vector
print("Ingrese números para rellenar el vector (introduzca un número negativo para terminar):")
for i in range(10):
    num = int(input("Ingrese un número: "))
    if num < 0:
        break
    vector.append(num)

# Imprimir el vector (sólo los elementos introducidos)
print("\nVector:")
for elemento in vector:
    print(elemento)
