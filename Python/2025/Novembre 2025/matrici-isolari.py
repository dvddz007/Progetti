from random import randint

def creaIsole(row, col, minimo, massimo, numIsole):
    """
        Non esclude le matrici sopravvposte.
    """
    matrice = [[randint(minimo, massimo) for c in range(col)] for r in range(row)]

    for i in range(numIsole):
        r = randint(0, row-2)  # escludo l'ultima riga
        c = randint(0, col-2)  # escludo l'ultima colonna
        print(f"Isola di {matrice[r][c]} che inzia in {(r, c)}")
        matrice[r][c+1] = matrice[r][c]
        matrice[r+1][c] = matrice[r][c]
        matrice[r+1][c+1] = matrice[r][c]
    print()
    return matrice


def checkIsole(matrice) -> bool:
    """
        Restituisce True se è presente almeno un'isola.
    """
    for r in range(len(matrice)-1):
        for c in range(len(matrice[r])-1):
            if matrice[r][c+1] == matrice[r][c] and matrice[r+1][c] == matrice[r][c] and matrice[r+1][c+1] == matrice[r][c]:
                return True
    return False

def stampaTabellare(matrice):
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] < 10:
                print("   " +  str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print("  " +  str(matrice[r][c]), end="")
            else:
                print(" " +  str(matrice[r][c]), end="")
        print()


matrice = creaIsole(10, 10, 0, 9, 5)
stampaTabellare(matrice)
print(checkIsole(matrice))
