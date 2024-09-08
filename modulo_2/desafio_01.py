"""
Crear una función que use lo visto de excepciones
para que tome por input() el número como str y
lo transforme directamente a float, sea entero o
decimal. Deberíamos pasar como argumento la
frase para mostrar en pantalla el pedido. Además,
deberíamos de volver a pedir, hasta que se pueda
hacer el ingreso de forma correcta.
A partir de ahora cada vez que tomemos un número
por teclado podemos hacer uso de esta función que
vamos a crear.
"""
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

#modo de uso
# Para solicitar un número entero
numero_entero = solicitarNumero("Ingrese un número entero: ", tipo=int)

# Para solicitar un número decimal
numero_flotante = solicitarNumero("Ingrese un número decimal: ", tipo=float)

# Sin especificar el tipo, por defecto acepta un número decimal
numero = solicitarNumero()