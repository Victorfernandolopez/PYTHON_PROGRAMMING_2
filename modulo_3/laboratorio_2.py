"""
Crear una clase “Persona” que sea la clase padre de otra
clase “Estudiante”.
La clase “Persona” su método __init__() debe de estar
preparado para recibir nombre y apellido. Además, esta
clase , debe tener un método para mostrar
nombre_completo() el cual debe mostrar el nombre
acompañado del apellido.
La otra clase “Estudiante”, debe de poder heredar de
“Persona”, y además recibir los argumentos nombre y
edad. También la clase “Estudiante”, recibe el valor
“carrera”, y además contar con un método
mostrar_carrera() . Las dos clases son obligatorias.
"""
class Persona:
    # Constructor de la clase Persona, inicializa los atributos nombre y apellido.
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    # Método para mostrar el nombre completo de la persona.
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

# Clase Estudiante que hereda de la clase Persona.
class Estudiante(Persona):
    # Constructor de la clase Estudiante, inicializa los atributos nombre, apellido y carrera.
    def __init__(self, nombre, apellido, carrera):
        super().__init__(nombre, apellido)
        self.carrera = carrera
    
    # Método para mostrar la carrera del estudiante.
    def mostrar_carrera(self):
        return f"Estudiante de la carrera {self.carrera}"

# Creando objetos de las clases.

persona1 = Persona("Juan", "Perez")
estudiante1 = Estudiante("Juan", "Perez", "Ingeniería en Computación")

# Mostrando los resultados.

print(persona1.nombre_completo())  # Imprime: Juan Perez
print(estudiante1.mostrar_carrera())  # Imprime: Estudiante de la carrera Ingeniería en Computación
