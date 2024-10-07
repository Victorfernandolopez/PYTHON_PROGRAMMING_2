"""
Desarrollar un programa de Python que cree una base de
datos de SQLite llamada productos.sqlite y una tabla
de nombre productos con las siguientes columnas:
(id,nombre,precio)
"""
#realizar el ejercicio con funciones, estructura solid y comentarios

import sqlite3

# creación de la base de datos

def crear_base_datos():
    conn = sqlite3.connect('productos.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Base de datos creada con éxito")

# creación de un nuevo producto

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    conn = sqlite3.connect('productos.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?,?)", (nombre, precio))
    conn.commit()
    conn.close()
    print("Producto agregado con éxito")
    
# lista de todos los productos

def listar_productos():
    conn = sqlite3.connect('productos.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    print("Productos:")
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
    

# borrar un producto

def borrar_producto(id_producto):
    conn = sqlite3.connect('productos.sqlite')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id_producto,))
    conn.commit()
    conn.close()
    print("Producto borrado con éxito")

# actualizar un producto

def actualizar_producto(id_producto, nombre, precio):
    conn = sqlite3.connect('productos.sqlite')
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET nombre=?, precio=? WHERE id=?", (nombre, precio, id_producto))
    conn.commit()
    conn.close()
    print("Producto actualizado con éxito")

# creación de la base de datos

# crear_base_datos()

# agregar un producto

# agregar_producto("Producto 1", 100)
# agregar_producto("Producto 2", 200)
# # lista de todos los productos

# listar_productos()

#borrar un producto

borrar_producto(3)

# # lista de todos los productos

# listar_productos()

# # actualizar un producto

# actualizar_producto(2, "Producto 2 actualizado", 200)

# # lista de todos los productos

# listar_productos()