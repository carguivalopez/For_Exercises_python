''' 
Ejercicio 11
Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
    • Todos los alumnos mayores de edad.
    • Los alumnos mayores (los que tienen más edad)
'''
#Ejercicio 11

# Inicializar listas para almacenar nombres y edades de los alumnos
nombres = []
edades = []

# Leer nombre y edad de cada alumno
print("Ingrese el nombre y la edad de cada alumno. Ingrese '*' para terminar.")

while True:
    nombre = input("Nombre del alumno: ")
    
    if nombre == '*':
        break
    
    edad = int(input("Edad del alumno: "))
    
    nombres.append(nombre)
    edades.append(edad)

# Mostrar todos los alumnos mayores de edad
print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print("- Nombre:", nombres[i], "- Edad:", edades[i])

# Encontrar el alumno mayor (el que tiene más edad)
indice_mayor = edades.index(max(edades))
print("\nAlumno mayor:")
print("- Nombre:", nombres[indice_mayor], "- Edad:", edades[indice_mayor])

