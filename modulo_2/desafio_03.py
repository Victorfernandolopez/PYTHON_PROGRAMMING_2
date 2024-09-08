"""
Al programa anterior, agregarle una opción de ver los
últimos 5 registros (opción 3 y salir pasa a opción 4).
Solo los últimos 5 eventos tomarlos directamente del
txt. Si nuestro archivo está vacío, mostrar el mensaje
“No hay registros”, en caso de que tengamos menos
registros que 5, solo mostrar los que se tenga en el
archivo hasta ese momento.

"""
import time

# Función para registrar el ingreso de un empleado
def registrarIngreso():
    nombre = input("Ingrese el nombre del empleado: ")
    hora = time.asctime()
    with open("registro_empleados.txt", "a") as archivo:
        archivo.write(f"Ingreso - Nombre: {nombre}, Hora: {hora}\n")
    print(f"Registro de ingreso completado para {nombre} a las {hora}.\n")

# Función para registrar el egreso de un empleado
def registrarEgreso():
    nombre = input("Ingrese el nombre del empleado: ")
    hora = time.asctime()
    with open("registro_empleados.txt", "a") as archivo:
        archivo.write(f"Egreso - Nombre: {nombre}, Hora: {hora}\n")
    print(f"Registro de egreso completado para {nombre} a las {hora}.\n")

# Función para mostrar los últimos 5 registros del archivo
def mostrarUltimosRegistros():
    try:
        with open("registro_empleados.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) == 0:
                print("No hay registros.")
            else:
                print("Últimos 5 registros:")
                for linea in lineas[-5:]:
                    print(linea.strip())
    except FileNotFoundError:
        print("No hay registros.")

# Función para solicitar un número con validación
def solicitarNumero(mensaje="Ingrese un número: ", tipo=int):
    while True:
        try:
            numero = tipo(input(mensaje))
            return numero
        except ValueError:
            if tipo == int:
                print("ERROR. Entrada no válida, debe ingresar un número entero.")
            elif tipo == float:
                print("ERROR. Entrada no válida, debe ingresar un número decimal.")

# Función principal que muestra el menú y utiliza match
def menu():
    while True:
        print("Menú:")
        print("1 - Ingreso de empleado")
        print("2 - Egreso de empleado")
        print("3 - Ver los últimos 5 registros")
        print("4 - Salir del sistema")
        
        opcion = solicitarNumero("Seleccione una opción: ", tipo=int)

        match opcion:
            case 1:
                registrarIngreso()
            case 2:
                registrarEgreso()
            case 3:
                mostrarUltimosRegistros()
            case 4:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.\n")

# Iniciar el programa
menu()