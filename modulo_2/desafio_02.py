"""
Hacer un pequeño programa con un menú muy sencillo:
Menú:
1 - Ingreso de empleado
2 - Egreso de empleado
3 - Salir del sistema
>>>
Este sistema es básico, lo utiliza el personal de seguridad que registra el nombre de la persona que ingresa (opción 1), y que egresa
del edificio (opción 2). 
Además, es necesario registrar el horario de los eventos se podría usar el módulo time, y la función asctime() que devuelve un str con fecha y hora.
Cuando se quiere salir del programa se usa la opción 3. Tanto el ingreso y el egreso se registra en un archivo txt. Cada renglón representa un registro.
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
        print("3 - Salir del sistema")
        
        opcion = solicitarNumero("Seleccione una opción: ", tipo=int)

        match opcion:
            case 1:
                registrarIngreso()
            case 2:
                registrarEgreso()
            case 3:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.\n")

# Iniciar el programa
menu()