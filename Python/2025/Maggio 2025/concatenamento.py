lista1 = ['a', 'b', 'c', 'd']
lista2 = ['1', '2', '3', '4']
liste_concatenate = []

for i in range(len(lista1 if lista1 > lista2 else lista2)):
    liste_concatenate.append(lista1[i])
    liste_concatenate.append(lista2[i])

print(liste_concatenate)
