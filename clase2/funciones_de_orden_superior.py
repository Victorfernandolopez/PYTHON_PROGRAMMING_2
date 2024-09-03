"""funciones que reciben otra funcion"""

#map
#lo primero que recibe map es la funcion que quiero que se ejecute, y lo segundo es la estructura a iterar

def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

numeros = [1,2,3,4]

#map devuelve un resultado, por eso devemos alojar lo devuelto en una variable, o como en ete caso usarlo en un print
print(list(map(cuadrado, numeros)))

#------------------------------------------------------------------------------
#filter
anios = [1800,1840,1871,1999,2000,2020,2021]

def bisiesto(anio):
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        return True
    return False
#recibe una funcion y una estructura iterable
#filter devuelve un resultado, por eso devemos alojar lo devuelto en una variable, o como en ete caso usarlo en un print

print(list(filter(bisiesto, anios)))#si la funcion le devuelve un TRUE va a guardar el resultado en la lista, y si le arroja un FALSE lo descarta

#------------------------------------------------------------------------------
#sorted
num = [9,4,8,1,3,7]
print(sorted(num))

#mas alla que de porsi sorted ordene los numeros de una estructura iterable, la magia de este recide en que uno podria alterar el orden en que desea que se ordenen las estructuras

#definir el orden resultante
lst = [ 'a', 'aba', 'asd','sdsds', 'asdasdasfasf', 'asasa']
#orden alfabetico
print(sorted(lst))

#orden segun mi criterio(orden segun la cantidad de letras)
def miorden(x):
    return len(x)

print(sorted(lst, key=miorden))

#orden de forma desendente
print(sorted(num, reverse= True))
