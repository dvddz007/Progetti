from random import randint

def creaMatrice(size: int, minimum: int, maximum: int) -> list[list[int]]:
    """
        Crea una matrice quadrata casuale.
    """
    matrice = []
    for r in range(size):
        riga = []
        for c in range(size):
            riga.append(randint(minimum, maximum))
        matrice.append(riga)
    return matrice


def trasponi(matrice: list[list[int]]) -> list[list[int]]:
    """
        Inverte le colonne in righe.
        Esempio:
            matrice =
                [
                    [1, 4, 7]
                    [2, 5, 8]
                    [3, 6, 9]
                ]

            matriceT =
                [
                    [1, 2, 3]
                    [4, 5, 6]
                    [7, 8, 9]
                ]
            
    """
    matriceT = [[0] * len(matrice[0]) for _ in range(len(matrice))]
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            matriceT[c][r] = matrice[r][c]
    return matriceT


def stampaTabellare(matrice: list[list[int]]) -> None:
    """
        Stampa in forma tabellare una matrice quadrata.
        Gestisce i numeri fino a 1000 escluso.
    """
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            val = matrice[r][c]
            if val < 10:
                print('   ' + str(val), end='')
            elif 10 <= val < 100:
                print('  ' + str(val), end='')
            else:
                print(' ' + str(val), end='')
        print()


matrice = creaMatrice(9, 5, 100)
print('Matrice casuale:')
stampaTabellare(matrice)

print()

matriceTrasposta = trasponi(matrice)
print('Matrice trasposta:')
stampaTabellare(matriceTrasposta)
