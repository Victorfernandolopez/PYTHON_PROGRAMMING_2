#sintaxis de una funcion
#palabra_reservada nombre_funcion(parametros)
#   codigo_a_ejecutar

#potencia
def potencia(b,e):
    return b**e

#usar la funcion potencia
print(potencia(2,3))

#alterar el orden de los parametros
print(potencia(e=2,b=3))

#-------------------------------------------------------------
#multiplicar
def multiplicar(a,b):
    return a*b

#usar la funcion multiplicar
print(multiplicar(2,3))

#-------------------------------------------------------------
#parametro por defecto
def multiplicar2(a, b=3):
    return a*b

#usar la funcion multiplicar2 con el parametro por defecto
print(multiplicar2(2))#puede solo pasarse un parametro y el otro lo toma por defecto
print(multiplicar2(2,6))#puede pasarse los 2 parametros y sobreescribir el parametro por defecto

#-------------------------------------------------------------
#pasar argumentos indefinidos

def sumar(*args): #toma el formato de tupla
    total = 0
    for numero in args:
        total += numero
    return total

#usar la funcion sumar
print(sumar(1,2,3,4,5))
print(sumar(1,2,3,4,5,6,7,8,9,10))

#--------------------------------------------------------------
#desempaquetar un args
def sumar2(a,*args):#el primer valor dado se va a asignar a a y el resto al args
    return sum(args) * a

#usar la funcion sumar2
print(sumar2(2,1,2,3,4,5)) #el primer valor dado se va aque multiplica al resto y el resto se suman
print(sumar2(3,1,2,3,4,5,6,7,8,9,10)) #el primer valor dado se va a que multiplica al resto y el resto se suman

#--------------------------------------------------------------
#KEYWORDS

def amigos(**kwargs): #toma el formato de diccionario
    for c,v in kwargs.items():
        print(f"Amigo {c}: {v}")

#usar la funcion amigos
amigos(juan=30, ana=28, pedro=35)

