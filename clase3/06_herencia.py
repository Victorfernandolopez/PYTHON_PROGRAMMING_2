class ClaseA:
    def __init__(self):
        self.a = 1

class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()#para que herede los atributos de la clase A en el init
        self.b = 1000

mi_objeto = ClaseB()
print(mi_objeto.a,mi_objeto.b)