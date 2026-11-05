import random


def stampaTabellare(matrice: list[list[int]]) -> None:
        for r in range(len(matrice)):
            for c in range(len(matrice[r])):
                val = matrice[r][c]
                if val < 10:
                    print(' '*3 + str(val), end='')
                elif 10 <= val < 100:
                    print(' '*2 + str(val), end='')
                else:
                    print(' '*1 + str(val), end='')
            print()


def creaMatrice(row: int, col: int, minimo: int, massimo: int) -> list[list[int]]:
        minimo, massimo = min(minimo, massimo), max(minimo, massimo)
        matrice = []
        for r in range(row):
            riga = []
            for c in range(col):
                riga.append(random.randint(minimo, massimo))
            matrice.append(riga)
        return matrice


def trasposta(matrice: list[list[int]]) -> list[list[int]]:
        matriceTrasposta = []
        #  prendo la prima colonna
        for c in range(len(matrice[0])):
            rigaTrasposta = []
            #  scorro le righe
            for r in range(len(matrice)):
                rigaTrasposta.append(matrice[r][c])
            matriceTrasposta.append(rigaTrasposta)
        return matriceTrasposta


def esercizio1() -> None:
    '''
        🟦 Matrici rettangolari
            Genera una matrice rettangolare A di dimensione 3×2 con valori interi casuali tra 0 e 9.
            Stampala in modo leggibile
            Stampa numero di righe e colonne

            Genera una matrice B di dimensione 2×4 con valori casuali.
            Verifica se il prodotto A · B è definito
            Se sì, calcola il prodotto
    '''
    def stampaLenRigCol(matrice: list[list[int]]) -> None:
        lenRiga = len(matrice)
        lenCol = len(matrice[0])

        for c in range(1, lenRiga):
            if len(matrice[c]) > lenCol:
                lenCol = len(matrice[c])

        print(
            f'Righe della matrice: {lenRiga}'
            '\n'
            f'Colonne della matrice: {lenCol}'
            )


    def isDefined(a: list[list[int]], b: list[list[int]]) -> bool:
        return len(a[0]) == len(b)


    A = creaMatrice(3, 2, 0, 9)

    print('Matrice Casuale A:')
    stampaTabellare(A)
    stampaLenRigCol(A)

    print()

    print('Matrice Casuale B:')
    B = creaMatrice(2, 4, 1, 10)
    stampaTabellare(B)

    if isDefined(A, B):
        colonne = len(A[0])
        righe = len(B)
        print(f'A e B sono definite e il risultato é: {colonne * righe}')
    else:
        print('A e B non sono definiti.')


def esercizio2() -> None:
    '''
        🟩 Trasposta
        Scrivi una funzione che riceva una matrice A e restituisca la sua trasposta.
        Genera una matrice rettangolare A di dimensione 4×3 con valori casuali.
        Calcola la trasposta

        Verifica che la trasposta abbia dimensione 3×4
    '''
    def isTrasposta(a: list[list[int]], b: list[list[int]]) -> bool:
        '''
            Non controlla i singoli valori.
        '''
        if len(a) == len(b[0]) and len(a[0]) == len(b):
            return True
        return False


    A = creaMatrice(4, 3, 1, 10)
    stampaTabellare(A)

    print()

    B = trasposta(A)
    stampaTabellare(B)

    print(isTrasposta(A, B))


def esercizio3() -> None:
    '''
        🟨 Matrici simmetriche
        Genera una matrice quadrata A di dimensione 3×3 con valori casuali.
        Calcola la sua trasposta
        Verifica se la matrice è simmetrica

        Genera una matrice simmetrica 3×3 partendo da valori casuali
        (cioè assicurandoti che A[i][j] = A[j][i]).
    '''


    def creaSimmetrica(size: int, minimo: int, massimo: int, separatore: int = 0) -> list[list[int]]:
        matrice = creaMatrice(size, size, minimo, massimo)
        for r in range(size):
            for c in range(r, size):
                if r == c:
                    matrice[r][c] = separatore
                else:
                    matrice[c][r] = matrice[r][c]    
        return matrice



    def isSimmetrica(matrice: list[list[int]]) -> bool:
        for r in range(len(matrice)):
            for c in range(r+1, len(matrice[r])):
                if matrice[r][c] != matrice[c][r]:
                    return False
        return True


    A = creaMatrice(3, 3, 1, 10)
    B = trasposta(A)
    stampaTabellare(B)
    print(isSimmetrica(B))
    
    A = creaSimmetrica(3, 3, 1, 10)
    stampaTabellare(A)
    print(isSimmetrica(A))


def esercizio4() -> None:
    '''
        🟧 Matrici perimetrali
        Genera una matrice quadrata n×n (con n scelto casualmente tra 3 e 6).
        Riempi solo il perimetro con numeri casuali
        Tutti gli elementi interni devono essere 0

        Scrivi una funzione che, data una matrice quadrata, restituisca la somma degli elementi del perimetro.
    '''

    def convertiPerimetrale(matrice: list[list[int]]) -> list[list[int]]:
        size = len(matrice)
        for r in range(len(matrice)):
            for c in range(len(matrice[r])):
                if not(r in (0, size-1) or c in (0, size-1)):
                    matrice[r][c] = 0
                else:
                    matrice[r][c] = random.randint(1, 10)
        return matrice


    def sommaPerimetrale(matrice: list[list[int]]) -> int:
        size = len(matrice)
        somma = sum(matrice[0]) + sum(matrice[size-1])
        for r in range(1, len(matrice)-1):
            somma += matrice[r][0] + matrice[r][size-1]
        return somma


    size = random.randint(3, 6)
    matrice = creaMatrice(size, size, 1, 10)
    perimetrale = convertiPerimetrale(matrice)
    stampaTabellare(perimetrale)
    print(f'Somma matrice perimetral: {sommaPerimetrale(perimetrale)}')


def esercizio5() -> None:
    '''
        🟥 Altri esercizi utili
        Scrivi una funzione che controlli se una matrice è rettangolare (tutte le righe della stessa lunghezza).

        Data una matrice qualsiasi, trova:
            massimo
            minimo
            somma totale degli elementi
    '''


    def isRettangolare(matrice: list[list[int]]) -> bool:
        lenght = len(matrice[0])
        for riga in matrice:
            if len(riga) == lenght:
                return False
        return True

    
    def findMin(matrice: list[list[int]]) -> int:
        size = len(matrice)
        minimo = min(matrice[0])

        for r in range(1, size):
            val = min(matrice[r])
            if val < minimo:
                minimo = val
        return minimo

    
    def findMax(matrice: list[list[int]]) -> int:
        size = len(matrice)
        massimo = max(matrice[0])

        for r in range(1, size):
            val = max(matrice[r])
            if val > massimo:
                massimo = val
        return massimo

    
    def totalSum(matrice: list[list[int]]) -> int:
        size = len(matrice)
        somma = sum(matrice[0])

        for r in range(1, size):
            somma += sum(matrice[r])
        return somma

    
    matrice = creaMatrice(3, 3, 1, 10)
    stampaTabellare(matrice)
    print(
        isRettangolare(matrice),
        '\n'
        f'Minimo: {findMin(matrice)}',
        '\n'
        f'Massimo: {findMax(matrice)}',
        '\n'
        f'Somma totale: {totalSum(matrice)}',
        )
