def sumar(a,b):
    if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
        raise TypeError("Los valores deben ser numéricos")
    return a + b

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(sumar(num1, num2))
    except Exception as e:
        print(e.__class__)
    else:
        break


print("fin de programa")