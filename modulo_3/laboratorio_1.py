"""
Crea una clase “Persona”. Con atributos nombre y edad.
Además, hay que crear un método “cumpleaños”, que
aumente en 1 la edad de la persona cuando se invoque
sobre un objeto creado con “Persona”.
Tendríamos que lograr ejecutar el siguiente código con
la clase creada:
p = Persona("Juan", 21)
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")
"""
class Persona:
    # Constructor de la clase Persona, inicializa los atributos nombre y edad.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método cumpleaños, que aumenta en 1 la edad de la persona.
    def cumpleaños(self):
        self.edad += 1
    
# Creamos un objeto de la clase Persona y lo ejecutamos.

p = Persona("Juan", 21)
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")

# Salida: Juan cumple 22 años