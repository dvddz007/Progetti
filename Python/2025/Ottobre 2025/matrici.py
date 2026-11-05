from random import randint

RIGHE = 5
COLONNE = 5
listaDiListe = []

minimo = 101
massimo = -1

for r in range(RIGHE):
    lista = []
    for c in range(COLONNE):
        x = randint(1, 100)
        if x < minimo:
            minimo = x
            minindex = (r, c)
        if x > massimo:
            massimo = x
            maxindex = (r, c)
        lista.append(x)
    listaDiListe.append(lista)

for r in range(len(listaDiListe)):
    for c in range(len(listaDiListe[r])):
        print(listaDiListe[r][c], end=" ")
    print(f"-> somma lista[{r}]: {sum(listaDiListe[r])}")

print()

somma = 0
for lista in listaDiListe:
    somma += sum(lista)
print(f"Somma di tutte le liste: {somma}")

print()

min_row, min_col = minindex
max_row, max_col = maxindex

print(
    f"Il numero più piccolo della matrice è: {minimo} nella colonna {min_col} e nella riga {min_row}"
    "\n"
    f"Il numero più grande della matrice è: {massimo} nella colonna {max_col} e nella riga {max_row}"
)

print()

print(
    f"Primo elemento della prima lista innestata: {listaDiListe[0][0]}"
    "\n"
    f"Ultimo elemento dell'ultima lista innestata: {listaDiListe[-1][-1]}"
)
