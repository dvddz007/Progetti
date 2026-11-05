from os import path
import string


file = input("Inserire il nome di un file da aprire: ") + ".txt"
while not path.exists(file):
    print(f"Il file {file} non esiste.")
    file = input("Inserire il nome di un file da aprire: ") + ".txt"

with open(file, encoding="utf-8") as fi:
    testo = fi.readlines()
    testo = testo[0].split()
    print(f"{testo = }")

parole = {}
lettere = {}

for parola in testo:
    #
    #    punctuation:
    #        Oggetto stringa contenente tutti i simboli di punteggiatura;
    #    
    #    makestrans:
    #        Crea una tabella di traduzione.
    #        Accetta tre parametri:
    #            (
    #                carattere da sostituire,
    #                carattere con cui sostituire,
    #                caratteri da rimuovere.
    #            )
    #        Se un carattere é presente nel terzo parametro, viene rimosso.
    #
    #    translate:
    #        Applica la tabella creata da maketrans.
    #        Rimuove i caratteri associati a None, gli altri vengono sostituiti o rimossi secondo la tabella.

    parola = parola.translate(str.maketrans('', '', string.punctuation))
    #  non sostituire nessun carattere, ma rimuovi quelli presenti nella punctuation.
    if parola not in parole:
        parole[parola] = 1
    else:
        parole[parola] += 1

    for lettera in parola:
        if lettera not in lettere:
            lettere[lettera] = 1
        else:
            lettere[lettera] += 1

for parola in parole:
    print(f'Parola: {parola} | Conteggio: {parole[parola]}')
    for lettera in parola:
        print(f'Lettera: {lettera} | Conteggio: {lettere[lettera]}')
    print()


maxParole = (max(parole.values()))
paroleRicorrenti = []

for parola in parole:
    if parole[parola] == maxParole:
        paroleRicorrenti.append(parola)

maxLettere = (max(lettere.values()))
lettereRicorrenti = []

for lettera in lettere:
    if lettere[lettera] == maxLettere:
        lettereRicorrenti.append(lettera)

print(
    f'Le parole piú ricorrenti sono: {paroleRicorrenti}. Conteggio parole: {maxParole}'
    '\n'
    f'Le lettere piú ricorrenti sono: {lettereRicorrenti}. Conteggio lettere: {maxLettere}'
    )
