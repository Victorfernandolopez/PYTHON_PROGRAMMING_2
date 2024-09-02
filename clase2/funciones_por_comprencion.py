#sintaxis
#nueva_lista = [expresion for elemento in iterable if condicion]

# expresion: Operación que se aplicará a cada elemento.
# elemento: El elemento del iterable actual.
# iterable: Cualquier objeto que se pueda iterar (como una lista, cadena, tupla, etc.).
# condicion: (Opcional) Filtra los elementos que cumplen con esta condición.


#crear lista de numeros secuenciales del 0 al 2000
lista =[i for i in range(2001)]
#ahora agrega que solo imprima los pares
lista = [i for i in lista if i % 2 == 0]  # este if es una condicion que filtra los numeros pares

print(lista)

