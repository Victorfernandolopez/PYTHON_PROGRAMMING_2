"""
Construir una función que se llame “promedio_variable”.
Esta función debe tomar un número arbitrario de
argumentos numéricos y devolver el promedio.
"""

import math
def promedio_variable(*args):
    if len(args) == 0:
        return 0
    resultado = sum(args)/ len(args)
    return int(resultado)

#solicitar numeros al usuario para calcular el promerdio
numeros = []
while True:
    numero = input("Ingrese un número (o 'salir' para terminar): ")
    if numero.lower() == 'salir':
        break
    else:
        numeros.append(int(numero))

#calcular el promedio
promedio = promedio_variable(*numeros)
print(promedio)