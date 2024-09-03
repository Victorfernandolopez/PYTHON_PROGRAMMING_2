print("hola\ncomoestas?\nbienvenido")
print("hola\tcomoestas?\tbienvenido")
print("hola\bcomoestas?\bbienvenido")

print("""
      el poema
      de mi vida
      en tres lineas""")

nombre = "Norman"
apellido = "Beltran"
edad = 15
print("nombre: ", nombre,"apellido: ", apellido,"edad: ",edad)
print(f"nombre: {nombre},apellido: {apellido},edad: {edad}")

print(r"c:\carpeta\nueva\tabla")#row (si quiero que no aga ningun formateo le pongo r)
print("c:\carpeta\\nueva\\tabla")

#METODOS STRINGS

#1. upper()
#Uso: Convierte todos los caracteres de un string a mayúsculas.
#Ejemplo:
texto = "hola mundo"
print(texto.upper())  # Output: "HOLA MUNDO"


# 2. lower()
# Uso: Convierte todos los caracteres de un string a minúsculas.
# Ejemplo:
texto = "HOLA MUNDO"
print(texto.lower())  # Output: "hola mundo"


# 3. strip()
# Uso: Elimina los espacios en blanco al inicio y al final del string.
# Ejemplo:
texto = "  hola mundo  "
print(texto.strip())  # Output: "hola mundo"


# 4. split(sep=None)
# Uso: Divide un string en una lista de substrings, utilizando el separador especificado (por defecto, separa por espacios).
# Ejemplo:
texto = "hola mundo"
print(texto.split())  # Output: ['hola', 'mundo']


# 5. join(iterable)
# Uso: Une los elementos de un iterable (como una lista) en un solo string, utilizando un separador.
# Ejemplo:
lista = ['hola', 'mundo']
print(" ".join(lista))  # Output: "hola mundo"


# 6. find(sub)
# Uso: Devuelve el índice de la primera aparición de un substring en un string. Retorna -1 si no se encuentra.
# Ejemplo:
texto = "hola mundo"
print(texto.find("mundo"))  # Output: 5


# 7. replace(old, new)
# Uso: Reemplaza todas las apariciones de un substring por otro.
# Ejemplo:
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # Output: "hola Python"


# 8. startswith(prefix)
# Uso: Devuelve True si el string comienza con el prefix especificado.
# Ejemplo:
texto = "hola mundo"
print(texto.startswith("hola"))  # Output: True


# 9. endswith(suffix)
# Uso: Devuelve True si el string termina con el suffix especificado.
# Ejemplo:
texto = "hola mundo"
print(texto.endswith("mundo"))  # Output: True


# 10. count(sub)
# Uso: Cuenta cuántas veces aparece un substring en un string.
# Ejemplo:
texto = "hola hola mundo"
print(texto.count("hola"))  # Output: 2


# 11. capitalize()
# Uso: Convierte el primer carácter del string a mayúscula y los demás a minúscula.
# Ejemplo:
texto = "hola mundo"
print(texto.capitalize())  # Output: "Hola mundo"


# 12. title()
# Uso: Convierte el primer carácter de cada palabra en mayúscula.
# Ejemplo:
texto = "hola mundo"
print(texto.title())  # Output: "Hola Mundo"


# 13. isalpha()
# Uso: Devuelve True si todos los caracteres del string son letras (y no está vacío).
# Ejemplo:
texto = "hola"
print(texto.isalpha())  # Output: True


# 14. isdigit()
# Uso: Devuelve True si todos los caracteres del string son dígitos.
# Ejemplo:
texto = "12345"
print(texto.isdigit())  # Output: True


# 15. islower()
# Uso: Devuelve True si todos los caracteres del string están en minúscula.
# Ejemplo:
texto = "hola mundo"
print(texto.islower())  # Output: True


# 16. isupper()
# Uso: Devuelve True si todos los caracteres del string están en mayúscula.
# Ejemplo:
texto = "HOLA MUNDO"
print(texto.isupper())  # Output: True


# 17. isspace()
# Uso: Devuelve True si el string contiene solo espacios en blanco.
# Ejemplo:
texto = "   "
print(texto.isspace())  # Output: True


# 18. ljust(width, fillchar)
# Uso: Justifica el string a la izquierda, rellenando con un carácter específico hasta alcanzar el ancho deseado.
# Ejemplo:
texto = "hola"
print(texto.ljust(10, '-'))  # Output: "hola------"


# 19. rjust(width, fillchar)
# Uso: Justifica el string a la derecha, rellenando con un carácter específico hasta alcanzar el ancho deseado.
# Ejemplo:
texto = "hola"
print(texto.rjust(10, '-'))  # Output: "------hola"


# 20. zfill(width)
# Uso: Rellena el string con ceros a la izquierda hasta alcanzar el ancho deseado.
# Ejemplo:
texto = "42"
print(texto.zfill(5))  # Output: "00042"


# 21. rfind(sub)
# Uso: Devuelve el índice de la última aparición de un substring en un string. Retorna -1 si no se encuentra.
# Ejemplo:
texto = "hola mundo mundo"
print(texto.rfind("mundo"))  # Output: 10


# 22. partition(sep)
# Uso: Divide el string en una tupla de tres elementos: la parte antes del separador, el separador en sí, y la parte después del separador.
# Ejemplo:
texto = "hola mundo"
print(texto.partition(" "))  # Output: ('hola', ' ', 'mundo')


# 23. rpartition(sep)
# Uso: Igual que partition(), pero divide el string a partir de la última aparición del separador.
# Ejemplo:
texto = "hola mundo mundo"
print(texto.rpartition(" "))  # Output: ('hola mundo', ' ', 'mundo')


# 24. swapcase()
# Uso: Invierte el caso de todos los caracteres en el string (mayúsculas a minúsculas y viceversa).
# Ejemplo:
texto = "Hola Mundo"
print(texto.swapcase())  # Output: "hOLA mUNDO"


# 25. center(width, fillchar)
# Uso: Centra el string en un campo de un ancho determinado, rellenando con un carácter específico.
# Ejemplo:
texto = "hola"
print(texto.center(10, '-'))  # Output: "--hola---"