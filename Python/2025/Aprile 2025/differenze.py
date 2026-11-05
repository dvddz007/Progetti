lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 5, 4]

differenze = []

for i in range(len(lista1)):
    if lista1[i] != lista2[i]:
        differenze.append(lista1[i])

print(differenze)
