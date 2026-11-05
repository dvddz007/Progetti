from random import randint
import os

name = input("Inserire il nome di un file: ")
while not os.path.exists(f"{name}.txt"):
    print(f"Il file {name}.txt non esiste. Riprova.")
    name = input("Inserire il nome di un file: ")
print(f"Il file {name}.txt esiste!", end="\n\n")

with open("testo.txt", "r", encoding="utf-8") as fi:
    #x = randint(1, len(fi.readlines())) #  readlines() porta il contatore di lettura all'ultima riga del file
    #fi.seek(0) #  riporta l'indice di lettura a 0
    #print(f"Frase n.{x}:")
    #for _ in range(x):
    #    frase = next(fi).strip()
    #print(frase)
    #print()

    righe = fi.readlines()
    x = randint(1, len(righe))
    print(f"Frase n.{x}:" + "\n" + righe[x-1].strip()) #  x-1 perchè la x parte da 1, mentre le frasi del testo non hanno indice 0
    print()
