"""
En matemática, se conoce a la sucesión de Fibonacci
como una sucesión infinita de números naturales en
la que cada término está determinado por la suma de
los dos términos anteriores.
Por ejemplo, empezando con el 0 y el 1, los primeros
20 términos son los siguientes:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
610, 987, 1597, 2584, 4181
"""

def fibonacci(cant_terminos):
    if cant_terminos>2:
        fibonacci = [0, 1]
        for _ in range(2, cant_terminos):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
    else:
        return "La cantidad debe ser mayor a 2"

fibonacci1 = fibonacci(2)
print(fibonacci1)



