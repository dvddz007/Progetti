from random import randint


def righePari1(matrice: list[list[int]]) -> list[list[int]]:
    for r in range(len(matrice)):
        if r % 2 == 0:
            for c in range(len(matrice[r])):
                matrice[r][c] = 1
    return matrice


def colonnePari1(matrice: list[list[int]]) -> list[list[int]]:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if c % 2 == 0:
                matrice[r][c] = 1
    return matrice


def colonneRighePari1(row, col) -> list[list[int]]:
    matrice = []
    for r in range(row):
        lista = []
        if r % 2 == 0:
            matrice.append([1] * col)
        for c in range(col):
            lista.append(1)
    return matrice

        

def stampa(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            val = matrice[r][c]
            if val < 10:
                print("  " + str(val), end="")
            elif 10 <= val < 100:
                print(" " + str(val), end="")
            else:
                print("" + str(val), end="")
        print()



a = [[1, 5, 2, 7, 2, 7], [2, 6, 3, 6], [2, 5, 0]]
stampa(righePari1(a))

print()

b = [[1, 5, 2, 7, 2, 7], [2, 6, 3, 6], [2, 5, 0]]
stampa(colonnePari1(b))

print()

c = colonneRighePari1(9, 5)
stampa(c)