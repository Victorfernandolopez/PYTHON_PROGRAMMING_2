#cuanto son los tipos basicos de datos en python

# enteros
x = 10
print(type(x))

# float
y = 2.5
print(type(y))

# booleanos
z = True
print(type(z))

# cadenas
s = "Hello, World!"
print(type(s))

#numeros complejos
c = 3 + 4j
print(type(c))


"--------------------------------------------------------"
#colecciones de datos
"""
-listas []
1. orden: cada elemento pertenece a un indice en la lista
2. mutable: capacidad de cambiar elementos, borrar o agregar elementos
3. repeticion: permite repetir elementos


-tuplas ()
1. orden: cada elemento pertenece a un indice en la tupla
2. no mutable:
3. repeticion: permite repetir elementos

- diccionarios {clave, valor}
1. no ordenada:
2. son mutables:
3. repeticion de elementos: claves no y valores si

- conjuntos {}
1. no ordenada:
2. son mutables:
3. repeticion: no permite repetir elementos

"""

lista = [1, 2, 3, "a", 3.14, True,[1,2,3]]

#accediendo a un elemento de la lista
print(lista[0])

#mutabilidad
#modificar un elemento 0
lista[0] = 100
print(lista)

#agregar un elemento alfinal de la lista
lista.append("nuevo elemento")
print(lista)

#agregar un elemento al indice 3
lista.insert(3, "elemento insertado")
print(lista)

#borrar un elemento de la lista
del lista[0]
print(lista)

#borrar un elemento y obtener el valor borrado
valor_borrado = lista.pop(0)
print(lista)
print(valor_borrado)

#-------------------------------------------


tupla = (1, 2, 3, "a", 3.14, True, [1,2,3])

#accediendo a un elemento de la tupla
print(tupla[0])

#ejemplo donde utilizar una tupla, en los meses del año, sabemos que no van a cambiar y solo son 12
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

#tupla de un solo elemento
un_elemento_tupla = ("elemento",)
print(type(un_elemento_tupla))

#-------------------------------------------

paises = { "USA": "Washington D.C.", "china": "Beijing", "Inglaterra": "London"}

print(f"la capital de china es {paises['china']}")

#agregar un nuevo país
paises["Australia"] = "Canberra"
print(paises)

#modificar una capital
paises["USA"] = "New York"
print(paises)

#eliminar un país
del paises["Inglaterra"]
print(paises)

#-------------------------------------------

conjunto = {1, 2, 3, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

#agregar un elemento al conjunto
conjunto.add(9)
print(conjunto)

#eliminar un elemento del conjunto
conjunto.discard(3)
print(conjunto)

#eliminar un elemento del conjunto 
conjunto.remove(5)#Si el elemento no existe, arroja una excepcion
print(conjunto)

#operaciones con conjuntos
# | (pipe) es la union de conjuntos
# & (and) es la interseccion de conjuntos
# ^ (xor) es la diferencia simétrica de conjuntos

union = conjunto | conjunto2
interseccion = conjunto & conjunto2
diferencia_simetrica = conjunto ^ conjunto2

print(f"Union: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia simétrica: {diferencia_simetrica}")

#listas slices
lista_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#extraer los elementos desde el indice 2 hasta el indice 5 (no incluido)
print(lista_slice[2:5])

#extraer los elementos desde el principio hasta el indice 5 (no incluido)
print(lista_slice[:5])

#extraer los elementos desde el indice 2 hasta el final
print(lista_slice[2:])

#extraer con saltos de 2
print(lista_slice[2:10:2])

#unpacking

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

#tupla unpacking

tupla = (1, 2, 3, 4, 5)
a,b,*c = tupla
print(a)
print(b)
print(c)

#id 

a = 1
b = 1
print(id(a))
print(id(b))

# is

a = 1
b = 1
print(a is b) #compara posicion de memoria

#walrus 

x = 10
if (y := x + 1) > 10:
    print("y es mayor que 10")

#sentencias de control

#if

x = 10
if x > 5:
    print("x es mayor que 5")

#elif   

x = 3
if x > 5:
    print("x es mayor que 5")
elif x == 3:
    print("x es igual a 3")

#if else 

x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")

#ternario
#sintaxis del ternario:
#variable = (valor si es verdadero IF condicion ELSE valor si es falso)
x = 10
print("x es mayor que 5" if x > 5 else "x no es mayor que 5")    
#si x es mayor que 5 se ejecuta el valor verdadero, y si no es mayor que 5 se ejecuta el valor por falso

#match 
opcion = 1
match opcion:
    case 1:
        print("opcion 1")
    case 2:
        print("opcion 2")
    case 3:
        print("opcion 3")
    case _:
        print("opcion desconocida")

#while

i = 0
while i < 5:
    print(i)
    i += 1