lst = [ 'a', 'aba', 'asd','sdsds', 'asdasdasfasf', 'asasa']

#esta funcion ordena segun la longitud del elemento
#def miorden(x):
#    return len(x)

#resolvemos la funcion de arriva como una funcion anonima
print(sorted(lst, key=lambda x: len(x)))

#sintaxix
#lambda cant_parametros: lo_que_retorna

nombres = ['jUan', ' ricardo','ANA', 'aLberto  ', ' maria', "Juana"]
print(list(map(lambda x: x.strip().upper() ,nombres)))#.strip saca los espacios en blanco

