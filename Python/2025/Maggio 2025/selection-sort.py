'''
generare una lista di 10 numeri casuali;
stampare la lista;
ordinare la lista con il selection sort;
stampare la lista.
'''

from random import randint


def selection_sort(lista: list[int]) -> list[int]:
    for i in range(len(lista)):
        minpos = i  # primo numero
        for j in range(i, len(lista)):  # da i in poi
            if lista[j] < lista[minpos]:  # se il numero più piccolo è maggiore del numero dopo
                minpos = j  # la posizione del numero più piccolo diventa j
        lista[i], lista[minpos] = lista[minpos], lista[i]  # si inverte il primo numero (minore) con il numero che si pensa minore
    return lista


for i in range(100):
    q = [randint(1, 1000) for i in range(10)]
    print(f"Lista originale: {q}")
    print(f"Lista ordinata: {selection_sort(q)}")
    print(sorted(q) == selection_sort(q))
