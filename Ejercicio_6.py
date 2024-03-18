''' 
Ejercicio 6
Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. 
Copia los elementos del vector en otro vector, pero en orden inverso, y muéstrale por la pantalla
'''


#Ejercicio 6 

# Crear un vector de 5 elementos de cadenas de caracteres
vector_original = []

# Inicializar el vector con datos leídos por el teclado
print("Ingrese 5 cadenas de caracteres:")
for _ in range(5):
    cadena = input("Ingrese una cadena: ")
    vector_original.append(cadena)

# Copiar los elementos del vector en otro vector en orden inverso
vector_inverso = vector_original[::-1]

# Mostrar los elementos del vector inverso por pantalla
print("\nVector inverso:")
for elemento in vector_inverso:
    print(elemento)
