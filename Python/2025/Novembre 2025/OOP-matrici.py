from random import randint


class Matrice:
    def __init__(self, row: int, col: int, minimum: int, maximum: int):
        self.righe = row
        self.colonne = col
        self.minimo = minimum
        self.massimo = maximum
        self.current = self.creaCasuale()

    def __getitem__(self, index: int):
        return self.current[index]

    def creaCasuale(self) -> list[list[int]]:
        matrice = []
        for r in range(self.righe):
            lista = []
            for c in range(self.colonne):
                lista.append(randint(self.minimo, self.massimo))
            matrice.append(lista)
        return matrice

    def __str__(self):
        return f"Matrice di {self.righe} righe e {self.colonne} colonne. Il valore minimo è {self.minimo} e il massimo é {self.massimo}."

    def creaSimmetrica(self, separator: int) -> list[list[int]]:
        matrice = [[separator] * self.colonne for _ in range(self.righe)]
        for r in range(self.righe):
            for c in range(r+1, self.colonne):
                if r != c:
                    val = randint(self.minimo, self.massimo)
                    matrice[r][c] = val
                    matrice[c][r] = val
        return matrice

    def creaPerimetrale(self, border: int) -> list[list[int]]:
        matrice = self.creaCasuale()
        for r in range(self.righe):
            for c in range(self.colonne):
                if r in (0, self.righe - 1) or c in (0, self.colonne - 1):
                    matrice[r][c] = border
        return matrice

    def creaIsolare(self, islandNumber: int, showIndexes=False) -> list[list[int]]:
        """
            Ignora la sovrapposizione di matrici.
        """
        matrice = [[randint(self.minimo, self.massimo) for _ in range(self.colonne)] for _ in range(self.righe)]

        for _ in range(islandNumber):
            r = randint(0, self.righe - 2)  # escludo l'ultima riga
            c = randint(0, self.colonne - 2)  # escludo l'ultima colonna
            if showIndexes:
                print(f"Isola di {matrice[r][c]} che inzia in {(r, c)}")
            matrice[r][c + 1] = matrice[r][c]
            matrice[r + 1][c] = matrice[r][c]
            matrice[r + 1][c + 1] = matrice[r][c]
        return matrice


def stampaTabellare(matrice):
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            if matrice[r][c] < 10:
                print("   " + str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print("  " + str(matrice[r][c]), end="")
            else:
                print(" " + str(matrice[r][c]), end="")
        print()


matrice = Matrice(9, 9, 1, 100)

casuale = matrice.creaCasuale()
print('Matrice casuale:')
stampaTabellare(casuale)
print(casuale[1][1])

print()

simmetrica = matrice.creaSimmetrica(5)
print('Matrice simmetrica:')
stampaTabellare(simmetrica)
print(simmetrica[1][1])

print()

perimetrale = matrice.creaPerimetrale(9)
print('Matrice perimetrale:')
stampaTabellare(perimetrale)
print(perimetrale[1][1])

print()

isolare = matrice.creaIsolare(2, True)
print('Matrice isolare:')
stampaTabellare(isolare)
print(isolare[1][1])
