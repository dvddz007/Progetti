'''
    Prendere in input un file di testo esistente, <file>.txt,
    un numero intero > 0 chiamato NUM_COL, numero di colonna,
    un intero > 0 chiamato NUM_CHR, numero di caratteri.

    Creare un file con il nome <file>-giustificato.txt contenente
    le parole del primo GIUSTIFICATE su NUM_COL colonne,
    ciascuna contenente NUM_CHR caratteri.

    # testo giustificato: formattazione che allinea a destra e sinistra i caratteri di un paragrafo.
'''

import os


def insert_dash(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]


file = input("Inserire il nome di un file di testo: ") + ".txt"
while not os.path.exists(file):
    print(f"Il file {file} non esiste. Inserire un file di testo valido.")
    file = input("Inserire il nome di un file: ")

print(f"Il file {file} esiste.")

to_check = f'{file.replace(".txt", "")}-giustificato.txt'
if os.path.exists(to_check):
    os.remove(to_check)
fg = open(to_check, "x")

with open(file, "r") as fi:
    testo = fi.read()

MAX_COL = 1
MAX_CHAR = 15
while MAX_CHAR <= 0:
    print("La quantità massima di caratteri deve essere superiore a 0: ")
    MAX_CHAR = int(input("Inserire il numero massimo di caratteri per riga: "))

print(testo)

for j in range(MAX_COL):
    '''#       WHILE?
    for i in range(space_index, MAX_CHAR):
        old_index = 0
        space_index = testo.find(" ", old_index)
        if space_index < MAX_CHAR:
            print(space_index)
            old_idex = space_index+1
            space_index = testo.find(" ", old_idex)
        elif space_index == MAX_CHAR:
            print(space_index, MAX_CHAR)
            print()
        else:
            pass'''
    
    space_index = 0
    old_index = space_index
    while space_index < MAX_CHAR:
        print(f"space index inizio: {space_index}")
        print(f"old index inizio: {old_index}")
        old_index = space_index + 1
        space_index = testo.find(" ", old_index)
        print(f"space index fine: {space_index}")
        print(f"old index inizio: {old_index}")
    print(space_index)


