from random import randint


def stampaMatrice(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] < 10:
                print('   ' + str(matrice[r][c]), end='')
            if 10 <= matrice[r][c] < 100:
                print('  ' + str(matrice[r][c]), end='')
            if 100 <= matrice[r][c] < 1000:
                print(' ' + str(matrice[r][c]), end='')
        print()


def creaMatriceCasuale(row: int, col: int, minimum: int, maximum: int) -> list[list[int]]:
    matrice = []
    for r in range(row):
        lista = []
        for c in range(col):
            lista.append(randint(minimum, maximum))
        matrice.append(lista)
    return matrice


def creaMatriceSimmetrica(row: int, col: int, minimum: int, maximum: int, delimiter: int) -> list[list[int]]:
    matrice = [[0] * col for _ in range(row)]
    for r in range(row):
        for c in range(r, col):
            x = randint(minimum, maximum)
            matrice[r][c] = x
            matrice[c][r] = x
            if r == c:
                matrice[r][c] = delimiter
    return matrice


def isSimmetrica(matrice: list[list[int]]) -> bool:
    for r in range(len(matrice)):
        for c in range(r, len(matrice[r])):
            if matrice[r][c] != matrice[c][r]:
                return False
    return True


def creaMatricePerimetrale(row: int, col: int, minimum: int, maximum: int, box: int) -> list[list[int]]:
    matrice = []
    for r in range(row):
        lista = []
        for c in range(col):
            if r in (0, row - 1) or c in (0, col - 1):
                lista.append(box)
            else:
                lista.append(randint(minimum, maximum))
        matrice.append(lista)
    return matrice


def isPerimetrale(matrice: list[list[int]]) -> bool:
    bordo = matrice[0][0]
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if (r in (0, len(matrice) - 1)) or (c in (0, len(matrice[r]) - 1)):
                if matrice[r][c] != bordo:
                    return False
    return True


def isIsolare(matrice: list[list[int]]) -> bool:
    for r in range(len(matrice) - 1):
        for c in range(len(matrice[r]) - 1):
            if matrice[r][c] == matrice[r][c + 1] and matrice[r][c] == matrice[r + 1][c] and matrice[r][c] == \
                    matrice[r + 1][c + 1]:
                return True
    return False


def verificaMatrice(matrice: list[list[int]]) -> None:
    risultati = {
        'simmetrica': isSimmetrica(matrice),
        'perimetrale': isPerimetrale(matrice),
        'isolare': isIsolare(matrice)
    }

    for key, value in risultati.items():
        print(f'É {key}? {value}')


LENR = 9
LENC = 9
minrange = 1
maxrange = 1000

matrice_casuale = creaMatriceCasuale(LENR, LENC, minrange, maxrange)
print(f'Matrice Casuale {LENR}x{LENC}: ')
stampaMatrice(matrice_casuale)
verificaMatrice(matrice_casuale)

print()

asse = 0
matrice_simmetrica = creaMatriceSimmetrica(LENR, LENC, minrange, maxrange, asse)
print(f'Matrice Simmetrica {LENR}x{LENC}: ')
stampaMatrice(matrice_simmetrica)
verificaMatrice(matrice_simmetrica)

print()

perimetro = 0
matrice_perimetrale = creaMatricePerimetrale(LENR, LENC, minrange, maxrange, perimetro)
print(f'Matrice Perimetrale {LENR}x{LENC}: ')
stampaMatrice(matrice_perimetrale)
verificaMatrice(matrice_perimetrale)

print()

minrange = 0
maxrange = 1
matrice_isolare = creaMatriceCasuale(LENR, LENC, minrange, maxrange)
print(f'Matrice Isolare {LENR}x{LENC}: ')
stampaMatrice(matrice_isolare)
verificaMatrice(matrice_isolare)
