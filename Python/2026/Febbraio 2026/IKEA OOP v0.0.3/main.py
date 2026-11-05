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
        "Digitare [ 4 ] per svuotare il carrello.\n"
        "Digitare [ 5 ] per visualizzare l'articolo più costoso.\n"
        "Digitare [ 0 ] per uscire dal programma."
        )

    scelta = int(input("Scegliere un'operazione: "))
    match scelta:
        case 0:
            break

        case 1:
            numeroGambe = int(input("\nInserire il numero di gambe dello sgabello:\n"))
            while numeroGambe < 3:
                print("Il numero delle gambe deve essere maggiore o uguale a 3.")
                numeroGambe = int(input("\nInserire il numero di gambe dello sgabello:\n"))
            altezzaGambe = int(input("\nInserire l'altezza delle gambe dello sgabello (cm):\n"))
            while altezzaGambe < 1:
                print("L'altezza dello gambe deve essere maggiore o uguale a 1cm.")
                altezzaGambe = int(input("\nInserire l'altezza delle gambe dello sgabello (cm):\n"))

            raggio = int(input("\nInserire il raggio dello sgabello (cm):\n"))
            while raggio < 1:
                print("Il raggio deve essere maggiore o uguale a 1cm.")
                raggio = int(input("\nInserire il raggio dello sgabello (cm):\n"))

            altezza = int(input("\nInserire l'altezza dello sgabello (cm):\n"))
            while altezza < 1:
                print("L'altezza deve essere maggiore o uguale a 1cm.")
                altezza = int(input("\nInserire l'altezza dello sgabello (cm):\n"))

            CARRELLO.append(Sgabello(numeroGambe, altezzaGambe, raggio, altezza))
        case 2:
            pass

        case 3:
            if len(CARRELLO) == 0:
                print("\nCarrello vuoto.")
            else:
                print(f"\nIl carrello contiene ({len(CARRELLO)}) articoli:\n")

                totale = 0
                for i, articolo in enumerate(CARRELLO):
                    print(f"{i}: {articolo}\nPrezzo: {locale.currency(articolo.prezzo(), grouping=True)}\n")
                    totale += articolo.prezzo()
                print(f"Prezzo totale: {locale.currency(totale, grouping=True)}")

        case 4:
            CARRELLO = []
            print("\nCarrello svuotato.")

        case 5:
            indiceMax = 0
            costoMax = CARRELLO[0].prezzo()
            for i in range(1, len(CARRELLO)):
                if costoMax < CARRELLO[i].prezzo():
                    indiceMax = i
                    costoMax = CARRELLO[i].prezzo()
            print(f"\nL'articolo più costoso è {indiceMax} e costa {locale.currency(costoMax, grouping=True)}")

        case _:
            print("------------------")
            print("L'operazione inserita non è valida. Riprova.")
print("\nFINE PROGRAMMA.")