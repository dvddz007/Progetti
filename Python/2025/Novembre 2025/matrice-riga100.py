from random import randint

def matriceRighe100(row, col, minimo, massimo):
    matrice = []
    for r in range(row):
        lista = []
        for c in range(col):
            lista.append(randint(minimo, massimo))
        matrice.append(lista)

    for _ in range(randint(1, row-1)):
        randomRow = randint(0, row-1)
        if sum(matrice[randomRow]) < 100:
            matrice[randomRow][0] += 100 - sum(matrice[randomRow])
        else:
            matrice[randomRow][0] -= 100 - sum(matrice[randomRow])
    return matrice


def stampaTabellare(matrice):
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            print(" " + str(matrice[r][c]), end="")
        print()

matrice= matriceRighe100(9, 9, 1, 10)
stampaTabellare(matrice)

for riga in matrice:
    print(sum(riga), end=" ")
