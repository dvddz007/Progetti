lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

def rimuovi_terzo(lista):
    i = 2
    while i < len(lista):
        lista.pop(i)
        i += 2
    return lista


print(rimuovi_terzo(lista))
