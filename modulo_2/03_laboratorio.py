"""
Crear un script que solicite al usuario el código de un país e imprima su nombre, de acuerdo con el siguiente diccionario:
# Diccionario código: país.
paises = {
        "ar": "Argentina",
        "es": "España",
        "us": "Estados Unidos",
        "fr": "Francia"
}
Si el código ingresado no se encuentra en el diccionario, debe imprimir un mensaje en pantalla y volver a preguntar. Si el usuario escribe “salir”, el programa debe terminar.
"""
#control de la entrada de datos
def entradaValida():
    while True:
        try:
            entrada = input("Ingrese el código del país (ej. ar, es, us...) o 'salir' para terminar: ").lower().strip()
            #verificar que no este vacia
            if not entrada:
                raise ValueError("La entrada está vacía.")
            return entrada
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

paises = {
        "ar": "Argentina",
        "es": "España",
        "us": "Estados Unidos",
        "fr": "Francia"
}

while True:
    entrada = entradaValida()
    if entrada == 'salir':
        print("saliendo del programa... ¡Hasta luego!")
        break
    if entrada in paises:
        print(f"el pais que busca es {paises[entrada]}.")
    else:
        print(f"El código '{entrada}' no está en la lista de paises. Intente con: {', '.join(paises.keys())}.")
