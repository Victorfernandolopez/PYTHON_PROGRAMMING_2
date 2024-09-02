#for con breack

for i in range(10):
    if i == 4:
        break#cuando i vale 4 termina el bucle
    print(i)
else:
    print("El bucle ha terminado")

#for con continue
for i in range(10):
    if i == 4:
        continue#de esta forma cuando es 4 saltea las instrucciones siguientes y vuelve a evaluar la condicion
    print(i)
else:
    print("El bucle ha terminado")