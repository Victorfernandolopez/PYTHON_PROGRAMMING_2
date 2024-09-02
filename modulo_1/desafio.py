"""
Dada 2 listas con números enteros, crear una tercera con los
números que pertenecen a ambas. Pero con la salvedad que
en esta tercera no debe tener elementos repetidos.
primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
Usar únicamente sentencias de control: condicionales y bucles.
También es probable que tengas que usar el operador de
pertenecía.
"""
#para armar una sola lista y no repetir elementos es recomendable usar un conjunto, el cual por propiedad propia no permite la repeticion de valores

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

#convertir las primeras 2 listas a conjunto
tercera = set(primera)|set(segunda) 
#otra opcion seria sumar las primeras 2 listas y luego convertirlas a un conjunto
cuarta = set(primera+segunda)
print(f"primer lista: {type(primera)}")
print(f"segunda lista: {type(segunda)}")
print(f"tercera lista: {type(tercera)}")
print(tercera)
print(f"cuarta lista: {type(cuarta)}")
print(cuarta)
