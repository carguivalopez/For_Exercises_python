''' 
Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. 
Luego programáticamente calcule el promedio de notas descontando la nota eliminada
'''
#Ejercicio 4

notas = [20, 15, 12, 11, 8, 4, 1]

# Eliminar la nota más baja sin usar la función min
nota_minima = notas[0]
indice_minimo = 0

for i in range(1, len(notas)):
    if notas[i] < nota_minima:
        nota_minima = notas[i]
        indice_minimo = i

nota_eliminada = notas.pop(indice_minimo)
print("Nota más baja eliminada:", nota_eliminada)

# Calcular el promedio de notas descontando la nota eliminada
promedio = sum(notas) / len(notas)
print("Promedio de notas descontando la nota eliminada:", promedio)
