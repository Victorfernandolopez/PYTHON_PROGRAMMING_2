class Animal:
    def __init__(self, animalsName):
        print(animalsName, "is an animal")

class Mammal(Animal):
    def __init__(self, Name):
        print(Name, "is a mammal.")
        super().__init__(Name)

class Dontfly(Mammal):
    def __init__(self, Name):
        print(Name, "cannot fly.")
        super().__init__(Name)

class DontSwim(Mammal):
    def __init__(self, Name):
        print(Name, "cannot swim.")
        super().__init__(Name)

class Cat(Dontfly, DontSwim):
    def __init__(self):
        print("A cat")
        super().__init__("cat")

cat = Cat()
print("")
bat = DontSwim("bat")