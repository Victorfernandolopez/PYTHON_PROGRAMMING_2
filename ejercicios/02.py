#crear la serie de fibonacci con comprencion de lista

n = 10  # Cantidad de términos que quieres en la serie
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, n)]

print(fibonacci)