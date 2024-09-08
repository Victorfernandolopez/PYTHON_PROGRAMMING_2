#crear un archivo y agregar contenido en el mismo
with open("archivo2.txt", "w") as f:
    f.write("alejandro dumas\n")
    f.write("jorge luis borges\n")
    f.write("stephen king\n")
    f.write("ernesto sabato\n")
#cada ves que ejecutamos el write este elimina el archivo y lo vuelve a crear un archivo y agregar contenido en el mismo