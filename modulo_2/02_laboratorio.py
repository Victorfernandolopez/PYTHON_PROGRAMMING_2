"""
Crear un programa que solicite dos números en consola e imprima el resultado de las cuatro operaciones aritméticas aplicadas sobre ellos. Por ejemplo (en rojo la entrada del usuario):
Escribe un número: 7
Escribe otro número: 5
a + b: 12
a - b: 2
a * b: 35
a / b: 1.4
Teniendo en cuenta lo siguiente:
● Si el usuario ingresa cualquier otra cosa que no sea un número, debe volver a preguntar, en ambos casos.
● Contemplar que el segundo número puede ser cero y, por ende, llegado el momento de la división el programa debe imprimir “No se puede dividir por cero”. Como restricción, no se pueden usar condicionales (if)
"""
#solicitar numero entero
def solicitarEntero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero  
        except ValueError:
            print("ERROR. Entrada no válida, debe ingresar un número entero.")
            
#control de division por 0
def divisionSegura(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "No se puede dividir por cero"

print("ingrese dos numero para realizar las operaciones aritmeticas (+,-,/,*)")
#solicitar datos
print("numero 1: ")
numero1 = solicitarEntero()
print("numero 2: ")
numero2 = solicitarEntero()

#claculos
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = divisionSegura(numero1,numero2)

print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division}")
