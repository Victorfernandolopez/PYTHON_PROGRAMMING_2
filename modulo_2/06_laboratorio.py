"""
Cree un algoritmo para volver al diccionario original
desde el archivo personas.txt creado en el ejercicio
anterior.
El nombre se tiene que recuperar en mayúsculas y
cada valor debe volver a ser del tipo entero.
El diccionario tendría que volver a verse como:
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
"""
#ejercicio resuelto suponiendo que el archivo de texto no es chico y tiene muchas lineas

# Crear el diccionario personas
personas = {}

# Abrir el archivo personas.txt en modo lectura
with open("personas.txt", "r") as p:
    # Leer la primera línea
    persona = p.readline().strip()

    # Usar un bucle while para leer hasta el final del archivo
    while persona:
        # Dividir la línea por el guion
        nombre, edad = persona.split("-")
        # Guardar los valores en el diccionario, el nombre en mayúscula y la edad como entero
        personas[nombre.capitalize()] = int(edad)
        # Leer la siguiente línea
        persona = p.readline().strip()

# Imprimir el diccionario
print(personas)

#-----------------------------------------------------
#ejercicio resuelto suponiendo que el archivo de texto es chico y no tiene muchas lineas
# Crear el diccionario personas
personas = {}

# Abrir el archivo personas.txt en modo lectura
with open("personas.txt", "r") as p:
    # Leer todas las líneas del archivo
    lineas = p.readlines()
    # Recorrer cada línea
    for linea in lineas:
        nombre, edad = linea.strip().split("-")
        personas[nombre.capitalize()] = int(edad)

# Imprimir el diccionario
print(personas)