import sqlite3

#funcion para crear tabla
def create_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            salario TEXT NOT NULL,
            depto TEXT NOT NULL,
            posicion TEXT NOT NULL,
            ingreso TEXT NOT NULL,
            edad NUMERIC NOT NULL
        )"""
    )
    conn.commit()#guardar los cambios en la base de datos

#funcion para insertar datos

def insertar():
    #datos a insertar con try-except para manejar posibles errores
    try:
        personas = (
            (1, 'Juan', '5000', 'RRHH', 'Jefe', '2020-01-01', 30),
            (2, 'Ana', '6000', 'RRHH', 'Encargada', '2020-02-01', 28),
            (3, 'Pedro', '4500', 'Contabilidad', 'Gerente', '2020-03-01', 32),
            (4, 'Maria', '5500', 'Contabilidad', 'Analista', '2020-04-01', 35),
            (5, 'Luis', '7000', 'Ventas', 'Gerente', '2020-08-01', 30),
            (6, 'Sofia', '6500', 'Ventas', 'Vendedora', '2020-09-01', 33)
        )
        for nid,nombre,salario,depto,posicion,ingreso,edad in personas:
            cursor.execute(
                "INSERT INTO empleados VALUES (?,?,?,?,?,?,?)", (nid, nombre, salario, depto, posicion, ingreso, edad)
            )
        conn.commit() #guardar los cambios en la base de datos
    except sqlite3.Error as error:
        print("Error al insertar los datos:", error)

#funcion para insertar un registro
def insertar_uno(nombre, salario, depto, posicion, ingreso, edad):
    try:
        cursor.execute(
            "INSERT INTO empleados (nombre, salario, depto, posicion, ingreso, edad) VALUES (?,?,?,?,?,?)",
            (nombre, salario, depto, posicion, ingreso, edad)
        )
        conn.commit() #guardar los cambios en la base de datos
    except sqlite3.Error as error:
        print("Error al insertar el registro:", error)

#funcion para consultar
def consultar():
    cursor.execute("SELECT * FROM empleados")
    filas = cursor.fetchall() #cursor.fetchall() devuelve todas las filas como una lista de tuplas
    for fila in filas:
        print(fila)

#funcion para consultar un registro

def consultar_uno():
    id = int(input("Ingrese el ID del empleado a consultar: "))
    cursor.execute("SELECT * FROM empleados WHERE id=?", (id,))
    fila = cursor.fetchone() #cursor.fetchone() devuelve la primera fila como una tupla
    if fila:
        print(fila)

#funcion para consultar un registro con LIKE
def consultar_like():
    nombre = input("Ingrese el nombre del empleado a consultar (con LIKE): ")
    cursor.execute("SELECT * FROM empleados WHERE nombre LIKE?", ('%' + nombre + '%',))
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

#funcion para borrar un registro

def borrar_uno():
    id = int(input("Ingrese el ID del empleado a borrar: "))
    cursor.execute("DELETE FROM empleados WHERE id=?", (id,))
    conn.commit() #guardar los cambios en la base de datos
    print("Registro borrado exitosamente.")

#funcion para actualizar un registro

def actualizar():
    id = int(input("Ingrese el ID del empleado a actualizar: "))
    nombre = input("Ingrese el nuevo nombre: ")
    salario = input("Ingrese el nuevo salario: ")
    cursor.execute(
        "UPDATE empleados SET nombre=?, salario=? WHERE id=?",
        (nombre, salario, id)
    )

#conectar con la base de datos
conn = sqlite3.connect('empleados.db')
#crear un cursor
cursor = conn.cursor() #permite ejecutar comandos SQL como insert, update, delete

#crear la tabla
#create_table()
#insertar()
#insertar_uno('Jose', '7500', 'Ventas', 'Gerente', '2020-10-01', 31)
#consultar()
#consultar_uno()
#consultar_like()
#borrar_uno()
#actualizar()

#cerrar la conexión
conn.close()