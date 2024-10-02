"""
Crear una clase cliente que pida por argumento los atributos: nombre_apellido(str) y el cuit (str, usar guiones del medio).
Únicamente tendrá un método que sea .mostrar_info() que muestra por pantalla el nombre del cliente y su cuit.
Ejemplo al crear una instancia: cliente1 = Cliente(nombreyapellido,cuit)
"""


class Cliente:
    def __init__(self, nombre_apellido, cuit):
        self.nombre_apellido = nombre_apellido
        self.cuiy = cuit

    def Mostrar_info(nombre_apellido, cuit):
        print(f"Nombre y Apellido: {nombre_apellido}")
        print(f"CUIT: {cuit}")

# Crear objetos

cliente1 = Cliente("Juan Perez", "20-12345678-9")
cliente2 = Cliente("Maria Garcia", "20-98765432-1")