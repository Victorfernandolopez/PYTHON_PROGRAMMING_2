"""
Ejercicio 1: Sumatoria
Crear un bucle que almacene en una variable la
suma de todos los elementos numéricos de una
lista, con excepción del último.
"""

lista = [1,2,3,4,5,6,7,8,9,10]
suma = 0
# Bucle que excluye el último elemento
for i in lista[:-1]:  # Usamos slicing para excluir el último elemento
    suma += i

print(suma)