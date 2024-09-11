class Alumno:
    #constructor
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    #sobreescritura del metodo str para mostrar el nombre y apellido en el mismo formato
    def __str__(self):
        return f"{self.apellido}. {self.nombre}"
    #metodos
    def saludar(self):
        print(f"hola {self.apellido}, {self.nombre}!")
    #metodo de encapsulacion
        #obtener los datos
    def get_apellido(self):
        return self.apellido
    def get_nombre(self):
        return self.nombre
        #modificar los datos
    def set_apellido(self, apellido):
        self.apellido = apellido
    def set_nombre(self, nombre):
        self.nombre = nombre
    #metodo de sobrecarga de operadores
    def __eq__(self, obj):
        if self.apellido == obj.apellido:
            return True
        else: 
            return False

#instanciar objeto
yo = Alumno("Pedro","Perez") #se crea el objeto yo
el = Alumno("Juan","Gonzales")
ella = Alumno("Ana","Gomes")
#imprimir el objeto utilizando __str__
print(yo,",",el,",",ella)
#imprimir el nombre y apellido encapsulado
print(f"{yo.get_apellido()}, {yo.get_nombre()}")
#usar el metodo saludar
yo.saludar() #ejecuta el metodo saludar predefinido en la clase Alumno
#usar sobrecarga de datos
espejo = Alumno("Marcelo","Perez")
if yo == espejo:
    print("Los objetos son iguales")
else:
    print("Los objetos son diferentes")