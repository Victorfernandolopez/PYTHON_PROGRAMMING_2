"""
Realizar un programa que permita agregar nuevos productos a la base de datos anterior a través de la consola. Se deberá solicitar para cada producto un id (numérico entero), un nombre (texto) y un precio(numérico entero). En el caso de los datos numéricos, volver a preguntar si el valor ingresado por el usuario es incorrecto.
Para acompañar al programa, hacer un menú como el siguiente:
Menú
1 – Agregar Productos
2 – Ver productos
3 – Salir
● La opción de agregar productos será la que despliegue la entrada de datos.
● La opción ver productos mostrara todos los productos cargados en la tabla.
● La opción de salir nos permite salir del programa.
"""
import laboratorio_1
#verificamos que el usuario ingreso un numero entero

def validar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("ERROR. Ingreso no válido. Ingrese un número entero.")

#creamos el menu
def menu():
    print("\nMenú")
    print("1 Agregar Productos")
    print("2 Ver productos")
    print("3 Salir")
    opcion = input("Ingrese una opción: ")
    return opcion
#ejecutamos el menu
while True:
    opcion = menu()
    if opcion == "1":
        laboratorio_1.agregar_producto()
    elif opcion == "2":
        laboratorio_1.listar_productos()
    elif opcion == "3":
        print("Gracias por utilizar el programa. Adiós.")
        break
    else:
        print("ERROR. Opción no válida. Intente de nuevo.")




