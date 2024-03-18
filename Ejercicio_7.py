''' 
Ejercicio 7
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''

#Ejercicio 7 

# Leer las 5 notas obtenidas por el alumno
notas = []

print("Ingrese las 5 notas del alumno (entre 0 y 10):")
for i in range(5):
    nota = float(input("Ingrese la nota {}:".format(i + 1)))
    while nota < 0 or nota > 10:
        print("La nota debe estar comprendida entre 0 y 10.")
        nota = float(input("Ingrese la nota {}:".format(i + 1)))
    notas.append(nota)

# Mostrar todas las notas
print("\nNotas del alumno:")
for i, nota in enumerate(notas, start=1):
    print("Nota {}: {}".format(i, nota))

# Calcular la nota media
nota_media = sum(notas) / len(notas)
print("\nNota media:", nota_media)

# Encontrar la nota más alta y la menor
nota_maxima = max(notas)
nota_minima = min(notas)

print("Nota más alta:", nota_maxima)
print("Nota menor:", nota_minima)

