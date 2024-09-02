"""
Utilizando un bucle “while”, elaborar un código
que imprima en pantalla cada uno de los
elementos de una lista y simultáneamente los
elimine, hasta quedar vacía.
"""
#definir lista
lista = [1,2,3,4,5,6,7,8,9]

#bucle
while True:
    #EL BUCLE DEBE EJECUTARSE MIENTRAS LA LISTA NO ESTE VACIA
    if len(lista) != 0:
        #mostrar el elemnto el primer elemento
        print(lista[0])
        #eliminar el elemento de la lista
        del lista[0]
    else:
        break
    