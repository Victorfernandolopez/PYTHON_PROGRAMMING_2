#METODO ANTIGUO DE APERTURA
#formato de apertura de archivo
"f = open('archivo.txt')"#abre el archivo en modo read

#leer el archivo
"print(f.read())"

#cerrar el archivo
"f.close()"

#METODO NUEVO DE APERTURA
with open("archivo.txt") as f:
    print(f.read()) #cuando termina el with, automaticamente cierra el archivo
#este formato solo nos sirve para leer archivos chicos

#para leer archivos grandes, es recomendable hacerlo linea por linea
with open("archivo.txt") as f:
    while linea:=f.readline(): #el while se va a terminar cuando se termine la ultima linea
        print(linea, end='')
