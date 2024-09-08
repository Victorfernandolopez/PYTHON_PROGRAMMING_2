"""
Se tiene una lista de personas como la siguiente:
["juan salvo","henry courtney","elizabeth bennet","marge simpson"]
Se desea crear una función que ponga mayúscula solo en la primera letra, tanto del nombre como del apellido, y que devuelva la lista con esta modificación.
Se puede usar funciones de orden superior para resolver el ejercicio, no hay limitaciones.
"""
personas = ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]

#usamos la funcion de orden superior map() que nos permite pasar como parametro una funcion y un objeto iterable, esta resuelve la funcion por cada objeto en el iterable. la funcion que le pasamos a map es una funcion lambda en la cual tratamos cada string aplicandole el metodo title, propio de los string que nos permite poner en mayusculas cada palabra que se procesa
def capitalize_persona(personas):
    return list(map(lambda persona: persona.title(),personas))

print(capitalize_persona(personas))

