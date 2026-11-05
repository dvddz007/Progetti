from random import randint

RIGHE = int(input("Inserire la lunghezza di righe della matrice: "))
COLONNE = int(input("Inserire la lunghezza di colonne della matrice: "))


def stampa_matrice(m: list[list[int]]):
    """
        Stampa una matrice.
    """
    for r in range(len(m)):
        for c in range(len(m[r])):
            print(m[r][c], end=" ")
        print()


def trova_min_max(m: list[list[int]]) -> tuple:
    """
        Trova il valore minimo e massimo in una matrice.

       Restituisce una tupla (minimo, massimo, minpos, maxpos)
       - minimo: int
       - massimo: int
       - minpos: tuple[int, int]
       - maxpos: tuple[int, int]
    """
    minimo = m[0][0]
    massimo = m[0][0]
    minpos = (0, 0)
    maxpos = (0, 0)
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] < minimo:
                minimo = m[r][c]
                minpos = (r, c)
            if m[r][c] > massimo:
                massimo = m[r][c]
                maxpos = (r, c)
    return minimo, massimo, minpos, maxpos


pari = 0
dispari = 0
n = int(input("Inserire un numero da cercare: "))
nrow = None
ncol = None
matrice = []
for r in range(RIGHE):
    lista = []
    for c in range(COLONNE):
        x = randint(1, 100)
        if x == n:
            nrow = r
            ncol = c
        if x % 2 == 0:
            pari += 1
        else:
            dispari += 1
        lista.append(x)
    matrice.append(lista)

stampa_matrice(matrice)

print()

somma = 0
for r in range(RIGHE):
    somma += matrice[r][0]
print(f"Somma prima colonna: {somma}")

somma = 0
for r in range(len(matrice)):
    somma += sum(matrice[r])

print()

minimo, massimo, minpos, maxpos = trova_min_max(matrice)

print(f"Media matrice: {somma / (RIGHE * COLONNE): .2f}")
print(f"Il valore più piccolo è {minimo} e si trova in {minpos}")
print(f"Il valore più grande è {massimo} e si trova in {maxpos}")
print(f"Elementi pari: {pari}")
print(f"Elementi dispari: {dispari}")

if nrow is None or ncol is None:
    print(f"Il numero {n} non è presente nella matrice")
else:
    print(f"Il numero {n} si trova nella riga {nrow} e colonna {ncol}")

'''
Creare e stampare una matrice
    Scrivi una funzione creaMatrice(size) che genera una matrice quadrata di dimensione size riempita con numeri casuali tra 1 e 9.
    Scrivi una funzione stampaMatrice(m) che la stampa in forma tabellare.
Somma degli elementi
    Scrivi una funzione che calcoli e restituisca la somma di tutti gli elementi della matrice.
    Somma delle diagonali
    Scrivi una funzione che calcoli la somma della diagonale principale e della diagonale secondaria.
Somma per righe e per colonne
Stampa la somma degli elementi per ogni riga e per ogni colonna.
'''


def creaMatrice(size: int) -> list[list[int]]:
    matrice = []
    for r in range(size):
        lista = []
        for c in range(size):
            lista.append(randint(1, 9))
        matrice.append(lista)
    return matrice


def stampa(matrice: list[list[int]]) -> None:
    for r in range(len(matrice)):
        for c in range(len(matrice)):
            if matrice[r][c] < 10:
                print("  " + str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print(" " + str(matrice[r][c]), end="")
        print()


def sommaMatrice(matrice: list[list[int]]) -> int:
    somma = 0
    for r in range(len(matrice)):
        somma += sum(matrice[r])
    return somma


def sommaDiagonali(matrice: list[list[int]]) -> tuple[int, int]:
    def diagonalePrincipale() -> int:
        somma_dp = 0
        for i in range(len(matrice)):
            somma_dp += matrice[i][i]
        return somma_dp

    def diagonaleSecondaria() -> int:
        somma_ds = 0
        i = 0
        j = -1
        while i != len(matrice):
            somma_ds += matrice[i][j]
            i += 1
            j -= 1
        return somma_ds

    return diagonalePrincipale(), diagonaleSecondaria()


def sommaRigheColonne(matrice: list[list[int]]) -> tuple[list[int], list[int]]:
    def sommaRighe() -> list[int]:
        somma_righe = []
        for r in range(len(matrice)):
            somma_righe.append(sum(matrice[r]))
        return somma_righe

    def sommaColonne() -> list[int]:
        somma_colonne = []
        for c in range(len(matrice)):
            somma_colonna = 0
            for r in range(len(matrice)):
                somma_colonna += matrice[r][c]
            somma_colonne.append(somma_colonna)
        return somma_colonne

    return sommaRighe(), sommaColonne()


'''
Verifica matrice diagonale
    Una matrice è diagonale se tutti gli elementi fuori dalla diagonale principale sono 0.
    Scrivi una funzione isDiagonale(m) che ritorna True se la matrice è diagonale, False altrimenti.
Matrice identità
    Scrivi una funzione creaIdentita(size) che crea una matrice identità (tutti 1 sulla diagonale principale e 0 altrove).
    Verifica che la matrice identità sia simmetrica (spoiler: lo è 😉).
Verifica matrice triangolare superiore
    Una matrice è triangolare superiore se tutti gli elementi sotto la diagonale principale sono 0.
    Scrivi isTriangolareSuperiore(m) che lo controlla.
Trasposta di una matrice
    Scrivi trasposta(m) che restituisce la trasposta (cioè righe e colonne scambiate).
'''


def isDiagonale(matrice: list[list[int]]) -> bool:
    for r in range(len(matrice)):
        for c in range(len(matrice)):
            if r == c:
                continue
            else:
                if matrice[r][c] != 0:
                    return False
    return True


def creaIdentita(size: int) -> list[list[int]]:
    matrice = []
    for r in range(size):
        lista = []
        for c in range(size):
            if r == c:
                lista.append(1)
            else:
                lista.append(0)
        matrice.append(lista)
    return matrice


def isTriangolareSuperiore(matrice: list[list[int]]) -> bool:
    for r in range(1, len(matrice)):  # ignoro la prima riga perchè non è compresa nel triangolo
        for c in range(len(matrice)):
            if r > c and matrice[r][c] != 0:  # r è maggiore di c dalla seconda riga fino a prima della metà matrice
                return False
    return True


def trasposta(matrice: list[list[int]]) -> list[list[int]]:
    RIGHE = len(matrice)
    COLONNE = len(matrice[0])
    matrice_trasposta = [[0] * RIGHE for _ in range(COLONNE)]
    for r in range(RIGHE):
        for c in range(COLONNE):
            matrice_trasposta[c][r] = matrice[r][c]
    return matrice_trasposta


'''
Prodotto di due matrici
    Scrivi una funzione prodottoMatrici(m1, m2) che restituisce il prodotto di due matrici quadrate.
Rotazione della matrice
    Scrivi una funzione ruota90(m) che restituisce la matrice ruotata di 90° in senso orario.
Controllo di simmetria con la trasposta
    Usa la funzione trasposta(m) e verifica se m == trasposta(m) per controllare la simmetria.
Creazione di una matrice perimetrale (ripasso)
    Ricrea la tua funzione creaPerimetrale(size) ma senza usare funzioni già scritte: fallo da zero.
'''


def prodottoMatrici(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    size = len(m1) if len(m1) == len(m2) else 0
    values = []
    for r in range(size):
        riga = []
        for c in range(size):
            somma = 0
            for k in range(size):
                somma += m1[r][k] * m2[k][c]
            riga.append(somma)
        values.append(riga)
    return values


def ruota90(matrice: list[list[int]]) -> list[list[int]]:
    size = len(matrice)
    ruotata = []
    for c in range(size):
        nuova_riga = []
        for r in range(size - 1, -1, -1):
            nuova_riga.append(matrice[r][c])
        ruotata.append(nuova_riga)
    return ruotata


def isTrasposta(matrice: list[list[int]]) -> bool:
    matrice_trasposta = trasposta(matrice)
    for r in range(len(matrice)):
        for c in range(len(matrice[0])):
            if matrice[r][c] != matrice_trasposta[r][c]:
                return False
    return True


def creaPerimetrale(size: int) -> list[list[int]]:
    matrice = []
    bordo = randint(1, 99)
    for r in range(size):
        lista = []
        for c in range(size):
            if (r in [0, size - 1]) or (c in [0, size - 1]):
                lista.append(bordo)
            else:
                lista.append(randint(1, 99))
        matrice.append(lista)
    return matrice


'''
Verifica "bordo costante"
    Scrivi una funzione che controlla se tutti i valori sul bordo (prima e ultima riga, prima e ultima colonna) sono uguali tra loro.
    (Simile alla tua isPerimetrale, ma con bordo già esistente.)
Specchia la matrice
    Scrivi una funzione che scambia le righe in ordine inverso, come se riflettessi la matrice verticalmente.
Conta numeri pari e dispari
    Conta quanti numeri pari e dispari ci sono nella matrice e stampa le percentuali.
'''


def bordoCostante(matrice: list[list[int]]) -> bool:
    bordo = matrice[0][0]
    for r in range(len(matrice)):
        for c in range(len(matrice[0])):
            if (r in [0, len(matrice) - 1]) or (c in [0, len(matrice) - 1]):
                if matrice[r][c] != bordo:
                    return False
    return True


def specchia(matrice: list[list[int]]) -> list[list[int]]:
    specchiata = []
    for riga in matrice:
        nuova = []
        for i in range(len(riga) - 1, -1, -1):  # partendo dall'ultimo elemento fino al primo
            nuova.append(riga[i])
        specchiata.append(nuova)
    return specchiata


def conteggio(matrice: list[list[int]]) -> tuple[int, int]:
    pari = 0
    dispari = 0
    for r in range(len(matrice)):
        for c in range(len(matrice[0])):
            if matrice[r][c] % 2 == 0:
                pari += 1
            else:
                dispari += 1
    return pari, dispari


def percentualiPariDispari(matrice: list[list[int]]) -> tuple[float, float]:
    pari, dispari = conteggio(matrice)
    totale = len(matrice) * len(matrice[0])
    return pari / totale * 100, dispari / totale * 100
