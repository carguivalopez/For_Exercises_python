''' 
Ejercicio 10
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene 
(por ejemplo, 30) y el nombre del mes. Debes usar un vector. Para simplificarlo vamos a suponer que febrero tiene 28 días.
'''

#Ejercicio 10 
# Definir un vector con los nombres de los meses y sus respectivos días
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Solicitar al usuario el número del mes
numero_mes = int(input("Ingrese el número del mes (1-12): "))

# Verificar si el número de mes es válido
if numero_mes < 1 or numero_mes > 12:
    print("Número de mes inválido.")
else:
    # Obtener el nombre del mes y el número de días
    nombre_mes = meses[numero_mes - 1]
    dias = dias_por_mes[numero_mes - 1]

    # Imprimir el nombre del mes y el número de días
    print("El mes de {} tiene {} días.".format(nombre_mes, dias))
