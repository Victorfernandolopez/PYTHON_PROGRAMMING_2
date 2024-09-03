#errores de semantica

try:
    a = 10/0
except:
    print("Error de división por cero")
#try: trata de resolver esto a=10/0 y si no podes dale  el control a except 

#se pueden capturar tantos exepcion como se desee y brindar un mensaje apropiado al usuario
try:
    a = 10/0 #zeroDivisionError
    int(list(1,2,3)) #TypeError
except ZeroDivisionError:
    print("Error de división por cero")
except TypeError:
    print("Hubo un error en la conversion")
print("fin del programa")
#una ves que encuentra el primer error en el try y pasa el control al excep correspondiente, continua el programa fuera del try: except:

"formato recomendado de uso"
#capturar  la excepcion
try:
    a = 20/0
except Exception as e:
    print("ocurrio un error", type(e), e.__class__)