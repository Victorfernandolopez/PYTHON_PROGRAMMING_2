"""
Tenemos una lista donde se registran los ingresos del
personal a un sistema:
personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
Contar los ingresos en un diccionario. La clave debería
de ser el nombre y el valor debería ser la cantidad de
ingresos.
"""
#registro de ingresos
personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

#inicializamos un diccionario vacío
contador_ingresos = {}

#recorrer la lista, agregar las personas en el diccionario, y contar los ingresos
for persona in personas:#persona toma el valor obtenido en persona
    if persona in contador_ingresos:
        contador_ingresos[persona] += 1 #si persona esta en el diccionario suma 1 al valor
    else:
        contador_ingresos[persona] = 1 # si persona no se encuentra en el diccionario se la agrega con valor 1
#de esta manera cada ves que se encuentre a una misma persona se le sumara uno a su valor de asistencia


#imprimir el diccionario
print(contador_ingresos)