from random import randint


def stampa(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice[0])):
            if matrice[r][c] < 10:
                print("  " + str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print(" " + str(matrice[r][c]), end="")
            else:
                print("" + str(matrice[r][c]), end="")
        print()


RIGHE = 3
COLONNE = 4
m = [[0] * COLONNE for _ in range(RIGHE)]

old_x = 0  # valore della posizione precedente in matrice
for r in range(RIGHE):
    for c in range(COLONNE):
        x = randint(old_x + 1, old_x + 10)
        m[r][c] = x
        old_x = x
stampa(m)
