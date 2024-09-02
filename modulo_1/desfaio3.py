"""
Crear una función que reciba un número como
argumento, ese número representará los segundos
que se quieren convertir a horas, minutos y segundos.
Por ejemplo, conversion(3600) retornaría el texto
“01:00:00” , en cambio si recibe 1000, devolverá
“00:16:40”
No se puede usar ninguna función built-in, ni
tampoco ningún módulo que haga la conversión. 
"""
# Solicitar la cantidad de segundos
cant_segundos = int(input("Ingrese la cantidad de segundos: "))

# Calcular la hora
hora = int(cant_segundos / 3600)

# Calcular los minutos
minutos = int((cant_segundos % 3600)/ 60)

# Calcular los segundos restantes
segundos = int((cant_segundos % 3600)% 60)

# Mostrar la conversión en formato hora:minuto:segundo
print(f"{hora:02d}:{minutos:02d}:{segundos:02d}")

