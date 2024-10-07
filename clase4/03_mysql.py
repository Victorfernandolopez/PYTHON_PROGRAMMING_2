import pymysql
import sys
# funcion para conectar con la base de datos
def conecxion():
    try:
        # conectar con la base de datos
        conn = pymysql.connect(host='localhost', user='root', password='bautista2018', db='peliculas')
        print("Conectado con la base de datos")
    except Exception as e:
        print("Error al conectar con la base de datos:", e)
        return "error"
    else:
        return conn

# funcion crear peliculas

def crear_peliculas(conn):
    try:
        with conn.cursor() as cursor:# crea un cursor para ejecutar SQL
            insertar = "INSERT INTO peliculas (titulo, anio) VALUES (%s, %s);"# Comando SQL para insertar una pelicula
            cursor.execute(insertar,("Star Wars: La Empire Strikes Back", 1980))# Insertar una pelicula
            cursor.execute(insertar,('Star Wars: Return of the Jedi', 1983))
            cursor.execute(insertar,('Star Wars: The Force Awakens', 2015))
            cursor.execute(insertar,('Inception', 2010))
            conn.commit()        
    except Exception as e:
        print("fallaron los insert", e)

# funcion crear peliculas versión 1

def crear_v1_peliculas(conn, titulo, anio):
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas (titulo, anio) VALUES (%s, %s);", (titulo, anio))
            conn.commit()
            print("Pelicula insertada correctamente")
    except Exception as e:
        print("Error al insertar la pelicula:", e)

# funcion para consultar todas las peliculas

def consultar_peliculas(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas;")
            filas = cursor.fetchall()# obtiene todas las filas de la consulta en formado de tuplas
            for fila in filas:
                print(fila)
        print("Peliculas consultadas correctamente")
    except Exception as e:
        print("Error al consultar las peliculas:", e)

# funcion para consultar una pelicula mayor a un año

def consultar_pelicula(conn, anio):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas WHERE anio > %s;", (anio,))
            filas = cursor.fetchall()
            for fila in filas:
                print(fila)
        print("Peliculas consultadas correctamente")
    except Exception as e:
        print("Error al consultar las peliculas:", e)

# funcion para consultar una pelicula versión 2 anio maxima

def consultar_v2_pelicula(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM peliculas ORDER BY anio DESC LIMIT 1;")
            fila = cursor.fetchone()
            print(fila)
        print("Pelicula consultada correctamente")
    except Exception as e:
        print("Error al consultar la pelicula:", e)

# funcion para actualizar anio de una pelicula

def actualizar_pelicula(conn):
    try:
        with conn.cursor() as cursor:
            id_pelicula = int(input("Ingrese el ID de la pelicula a actualizar: "))
            anio_nuevo = int(input("Ingrese el nuevo año de la pelicula: "))
            cursor.execute("UPDATE peliculas SET anio = %s WHERE id = %s;", (anio_nuevo, id_pelicula))
            conn.commit()
            print("Pelicula actualizada correctamente")
    except Exception as e:
        print("Error al actualizar la pelicula:", e)

# funcion para borrar una pelicula por id

def borrar_pelicula(conn):
    try:
        with conn.cursor() as cursor:
            id_pelicula = int(input("Ingrese el ID de la pelicula a borrar: "))
            cursor.execute("DELETE FROM peliculas WHERE id = %s;", (id_pelicula,))
            conn.commit()
            print("Pelicula borrada correctamente")
    except Exception as e:
        print("Error al borrar la pelicula:", e)

conn = conecxion()
if conn == "error":
    sys.exit()

#crear_peliculas(conn)
#crear_v1_peliculas(conn, "Furiosa", 2024)
#consultar_peliculas(conn)
#consultar_pelicula(conn,2020)
#consultar_v2_pelicula(conn)
#actualizar_pelicula(conn)
#borrar_pelicula(conn)
conn.close()