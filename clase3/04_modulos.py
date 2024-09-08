from datetime import date
#import datetime (importa toda la libreria apesar de que no la utilicemos)
#import datetime as dt(ponemos el alias para referirnos a la libreria)

hoy = date.today()
cumple = date(1988,12,6)
print(hoy)

victor = abs(hoy-cumple)

print(hoy, victor)