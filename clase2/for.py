#FOR
#iterar datos
amigos = ["ana", "juan", "maria", "jose", "pablo"]
for i in amigos:
    print("un amigo",i)

#enumerar datos
for indice, amigo in enumerate(amigos):#enumerate devuelve un indice y el elemnto
    print(f"Amigo {indice+1}: {amigo}")

#recorrer en una sola iteracion las 2 listas
apodos = ["any", "jhon","mar","pepe","cachito"]

for amigos,apodos in zip(amigos,apodos):#recorrer en una sola iteracion las 2 listas
    print(f"Amigo: {amigos}, Apodo: {apodos}")

#ITERACION EN DICCIONARIOS

#.items()
personas = {
    "juan": 30,
    "ana": 28,
    "pedro": 35
}
for nombre, edad in personas.items(): #recorre el diccionario obteniendo su clave y valor
    print(f"Nombre: {nombre}, Edad: {edad}")

#.key()
for nombre in personas.keys(): #recorre solo las claves del diccionario
    print(nombre)

#.values()
for edad in personas.values(): #recorre solo los valores del diccionario
    print(edad)

#RANGE()

for i in range(10): #recorre desde 0 hasta n-1
    print(i)

for i in range(2, 10):#recorre desde el 2 hasta n-1
    print(i)

for i in range(5,50,10): #recorre desde el 5 hasta n-1 de 10 saltos
    print(i)

#imprimir desde el 100 hasta el 80 inclusibe en ese orden
for i in range(100,79,-1):
    print(i)

