from random import randint


def creaMatrice(row: int, col: int, minimo: int, massimo: int) -> list[list[int]]:
    matrice = []
    for r in range(row):
        lista = []
        for c in range(col):
            lista.append(randint(minimo, massimo))
        matrice.append(lista)
    return matrice


def checkIsola(matrice: list[list[int]]) -> bool:
    for r in range(len(matrice) - 1):
        for c in range(len(matrice[r]) - 1):
            if (matrice[r][c] == matrice[r][c + 1]) and (matrice[r][c] == matrice[r + 1][c]) and (
                    matrice[r][c] == matrice[r + 1][c + 1]):
                return True
    return False


def stampa(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            print(matrice[r][c], end=" ")
        print()


cases = 0
m = creaMatrice(8, 8, 0, 1)
while checkIsola(m):
    m = creaMatrice(8, 8, 0, 1)
    stampa(m)
    print(checkIsola(m), end="\n\n")
    cases += 1
print(cases)
