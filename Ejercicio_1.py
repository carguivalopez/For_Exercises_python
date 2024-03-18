''' 
Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y 
crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado. 
Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, el array contendrá 3, 6, 9, 12, 15. 
Muéstralos por pantalla usando otra función distinta
'''

#Ejercicio 1

def llenar_arreglo(tamaño, multiplicador):
    arreglo = []
    for i in range(1, tamaño + 1):
        arreglo.append(i * multiplicador)
    return arreglo

def mostrar_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento, end=" ")

tamaño = int(input("Ingrese el tamaño del arreglo: "))
multiplicador = int(input("Ingrese el número para los múltiplos: "))

mi_arreglo = llenar_arreglo(tamaño, multiplicador)
print("El arreglo lleno es:")
mostrar_arreglo(mi_arreglo)






