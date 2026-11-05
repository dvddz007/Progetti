from Cassettiera import Cassettiera
from Sgabello import Sgabello
from random import randint
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


CARRELLO = []

print(
    "------------------\n"
    "Simulazione IKEA"
    )
while True:
    print(
        "------------------\n\n"
        "Digitare [ 1 ] per acquistare uno sgabello.\n"
        "Digitare [ 2 ] per acquistare una cassettiera.\n"
        "Digitare [ 3 ] per stampare il carrello.\n"
        "Digitare [ 4 ] per rimuovere un articolo dal carrello.\n"
        "Digitare [ 5 ] per svuotare il carrello.\n"
        "Digitare [ 6 ] per visualizzare l'articolo più costoso.\n"
        "Digitare [ 8 ] per inserire uno sgabello casuale.\n"
        "Digitare [ 9 ] per inserire una cassettiera casuale.\n"
        "Digitare [ 0 ] per uscire dal programma."
        )
    
    #  opzione per aggiungere delle stringhe dentro la cassettiera.

    scelta = int(input("Scegliere un'operazione: "))
    match scelta:
        case 0:
            break

        case 1:
            try:
                numeroGambe = int(input("\nInserire il numero di gambe dello sgabello:\n"))
                altezzaGambe = int(input("\nInserire l'altezza delle gambe dello sgabello (cm):\n"))
                raggio = int(input("\nInserire il raggio dello sgabello (cm):\n"))
                altezza = int(input("\nInserire l'altezza dello sgabello (cm):\n"))
                CARRELLO.append(Sgabello(numeroGambe, altezzaGambe, raggio, altezza))
            except ValueError:
                print("\nUn valore inserito non è valido.")
        case 2:
            try:
                numeroCassetti = int(input("\nInserire il numero di cassetti della cassettiera:\n"))
                materiale = input("\nScegliere il materiale della cassettiera:\n").lower()
                CARRELLO.append(Cassettiera(numeroCassetti, materiale))
            except ValueError:
                print("\nUn valore inserito non è valido.")

        case 3:
            if len(CARRELLO) == 0:
                print("\nCarrello vuoto.")
            else:
                print(f"\nIl carrello contiene ({len(CARRELLO)}) articoli:\n")

                totale = 0
                for i in range(len(CARRELLO)):
                    print(f"#{i+1}: {CARRELLO[i]}\nPrezzo: {locale.currency(CARRELLO[i].prezzo(), grouping=True)}\n")
                    totale += CARRELLO[i].prezzo()
                print(f"Prezzo totale: {locale.currency(totale, grouping=True)}")

        case 4:
            print(
                "Inserire [ 0 ] per annullare l'operazione."
                "\nInserire l'articolo da rimuovere\n"
                "es. 1, 2, 3..."
                  )
            try:
                indice = int(input(""))
                if indice == 0:
                    continue
                CARRELLO.pop(indice - 1)
            except ValueError:
                print("\nUn valore inserito non è valido.")
            except IndexError:
                print("\nL'elemento inserito non esiste.")
            else:
                print(f"\nL'articolo {indice} è stato rimosso.")

        case 5:
            print("\nSei sicuro di voler CANCELLARE il carrello?\n")
            try:
                conferma = input("[s/n] ").lower()
                while (conferma != "s") and (conferma != "n"):
                    print("L'input inserito non è valido. Riprova.\n")
                    conferma = input("[ s/n ]").lower()
                if conferma == "n":
                    continue
            except ValueError:
                print("\nUn valore inserito non è valido.")

            CARRELLO.clear()
            print("\nCarrello svuotato.")

        case 6:
            indiceMax = 0
            costoMax = CARRELLO[0].prezzo()
            for i in range(1, len(CARRELLO)):
                if costoMax < CARRELLO[i].prezzo():
                    indiceMax = i + 1
                    costoMax = CARRELLO[i].prezzo()
            print(f"\nL'articolo più costoso è ({indiceMax}) e costa {locale.currency(costoMax, grouping=True)}")

        case 8:
            CARRELLO.append(Sgabello(
                randint(3, 5),
                randint(10, 75),
                randint(50, 80),
                randint(100, 150)
            ))
            print("\nUno sgabello casuale è stato aggiunto al carrello.")

        case 9:
            materiale = "legno" if randint(0, 1) == 0 else "plastica"
            CARRELLO.append(Cassettiera(
                randint(1, 3),
                materiale
            ))
            print("\nUna cassettiera casuale è stata aggiunta al carrello.")

        case _:
            print("------------------")
            print("L'operazione inserita non è valida. Riprova.")
print("\nFINE PROGRAMMA.")