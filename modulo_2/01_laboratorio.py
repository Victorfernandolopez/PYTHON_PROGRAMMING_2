"""
Cree una función llamada “superior”, que reciba por
argumento una función y una lista. La función que se
pasa por argumento a superior debe elevar al cubo un
número y retornarlo. Para que luego al aplicarla en la
de orden superior, esa operación se realice miembro
a miembro de la lista.
Para finalizar la función “superior” debe de devolver
una nueva lista.
"""

# Función superior
def superior(cubo, lista):
    try:
        nueva_lista = [cubo(i) for i in lista]
    except TypeError as e:
        print(f"Error: {e}. Asegúrate de que la lista solo contenga números.")
        nueva_lista = []
    except Exception as e:
        print(f"Error inesperado: {e}")
        nueva_lista = []
    return nueva_lista

# Función cúbica
def cubo(numero):
    try:
        return numero**3
    except TypeError as e:
        print(f"Error: {e}. Asegúrate de que 'numero' sea un número válido.")
        return None

# Obtener número
def obtener_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
            break  
        except ValueError:
            print("Error: Debes introducir un número válido.")
    return numero

# Lista de números
lista = []
while True:
    try:
        opcion = input("¿Desea agregar números a la lista? (si/no): ").strip().lower()
        if opcion == 'si':
            numeros = obtener_numero()
            lista.append(numeros)
        elif opcion == 'no':
            break
        else:
            print("Error: Opción incorrecta. Vuelve a intentarlo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

print(f"Tu lista quedó conformada por los siguientes números: {lista}")
print(f"La nueva lista con los números al cubo es: {superior(cubo, lista)}")
