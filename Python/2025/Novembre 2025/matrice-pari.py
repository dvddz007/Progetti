'''
Scrivere un funzione creaPari(row, col, minimo, massimo):
che crea e restituisce una matrice di row righe e col colonne,
contenente tutti numeri pari random compresi tra min e max.
'''

from random import randint
# from keyboard import is_pressed
# from time import sleep


def stampa(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] < 10:
                print("   " + str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print("  " + str(matrice[r][c]), end="")
            else:
                print(" " + str(matrice[r][c]), end="")
        print()


def creaPari(row: int, col: int, minimo: int, massimo: int) -> list[list[int]]:
    matrice = []
    for r in range(row):
        lista = []
        for c in range(col):
            x = randint(minimo, massimo)
            if x % 2 == 0:
                lista.append(x)
            else:
                lista.append(x + 1)
        matrice.append(lista)
    return matrice


def isPari(matrice: list[list[int]]) -> bool:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] % 2 != 0:
                return False
    return True


minimo = randint(1, 100)
massimo = randint(minimo, minimo * 2)
matrice = creaPari(randint(1, 10), randint(1, 10), minimo, massimo)
print("Matrice:")
stampa(matrice)
print("La matrice è pari" if isPari(matrice) else "La matrice non è pari", "\n")
