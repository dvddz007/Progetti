import os.path
import string


def primo(numero: int) -> bool:
    """
        Prende un intero e restituisce un booleano.
    """
    if numero <= 1:
        return False
    if numero == 2 or numero == 3:
        return True
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True


file = input("Inserire il nome di un file: ")
while not os.path.exists(file):
    print(f"Il file {file} non esiste. Inserire un file valido.")
    file = input("Inserire il nome di un file: ")

print(f"Il file {file} esiste.")

with open(file, "r") as fi:
    text = fi.read()

print(f"Testo non formattato: \n{text}")
print()
#       translate traduce una stringa seguendo una tabella di traduzione.
#       maketrans(char_da_sostituire, char_sostituitivi, char da rimuovere) e ne crea una tabella di traduzione.
#       punctuation è una stringa che contiene tutti i caratteri di punteggiatura standard.
text = text.translate(str.maketrans("", "", string.punctuation))
text = text.split()

i = len(text) - 1

while i >= 0:
    if primo(len(text[i])):
        text.pop(i)
    i -= 1

print(f"Testo senza parole prime: \n{text}")
