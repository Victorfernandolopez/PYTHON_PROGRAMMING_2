import csv

with open('peliculas.top_1000.csv') as file:
    reader = csv.DictReader(file) # leer los datos del csv como diccionarios
    for fila in reader:# recorre cada fila del csv
        print(fila["Movie Name"],fila['Watch Time'])# imprime el nombre de la pelicula y el tiempo que la vió