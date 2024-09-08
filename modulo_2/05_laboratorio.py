"""
Cree un algoritmo para guarda cada una de las
personas del diccionario personas en un txt.
El nombre se tiene que guardar en minúsculas y
cada persona debe quedar en un renglón con un
guión del medio separando el nombre y la edad.
Ejemplo dentro del personas.txt se tendría que ver:
roberto-20
romina-32
"""
personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}

#abrir un archivo con whit
with open("personas.txt","w") as f:
    #iterar sobre el diccionario obteniendo el nombre y la edad
    for clave,valor in personas.items():
        #formatear el nombre (nombre.lower() + "-" + str(edad))
        f.write(f"{clave.lower()}-{valor}\n")