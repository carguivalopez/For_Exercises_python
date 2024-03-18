'''
Dado el siguiente arreglo de números:
[1, 5, 8, 3, 30, 9, 13]
Imprimir en pantalla programáticamente los números impares mayores a 3
''' 
#Ejercicio 3


numeros = [1, 5, 8, 3, 30, 9, 13]

print("Números impares mayores a 3:")
for num in numeros:
    if num % 2 != 0 and num > 3:
        print(num)
