#LISTAS POR COMPRENCION
#ejercicio: de la siguiente lista filtrar los nombres que empiecen con a
personas = ["susana","tamara","ana","susana","tomas","ana","analia","alberto"]
nueva_listaPersona = [nombre for nombre in personas if nombre[0]=="a"]
print(nueva_listaPersona)
