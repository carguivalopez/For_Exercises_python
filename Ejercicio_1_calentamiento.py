'''
Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y 
crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado.
 Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, el array contendrá 3, 6, 9, 12, 15. 
 Muestralos por pantalla usando otra función distinta.
 ''' 

 #Ejercicio de calentamiento 1

n = int(input(u"Ingrese el tamaño del areglo : "))
m = int(input(u"ingrese el numero de multiplos :"))
A = []
for i in range (0,n):
    A.append(i*m)
    print (A)

