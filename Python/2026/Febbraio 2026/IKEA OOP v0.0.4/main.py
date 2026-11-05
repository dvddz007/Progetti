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
            numeroCassetti = int(input("\nInserire il numero di cassetti della cassettiera:\n"))
            while (numeroCassetti < 2) or (numeroCassetti > 3):
                print("Il numero di cassetti deve essere maggiore di 1 e minore di 3")
                numeroCassetti = int(input("\nInserire il numero di cassetti della cassettiera:\n"))

            materiale = input("\nScegliere il materiale della cassettiera:\n").lower()
            while (materiale != "plastica") and (materiale != "legno"):
                print("Il materiale può essere plastica o legno.")
                materiale = input("\nScegliere il materiale della cassettiera:\n").lower()
        
            CARRELLO.append(Cassettiera(numeroCassetti, materiale))
        case 3:
            if len(CARRELLO) == 0:
                print("\nCarrello vuoto.")
            else:
                print(f"\nIl carrello contiene ({len(CARRELLO)}) articoli:\n")

                totale = 0
                for i, articolo in enumerate(CARRELLO):
                    print(f"#{i+1}: {articolo}\nPrezzo: {locale.currency(articolo.prezzo(), grouping=True)}\n")
                    totale += articolo.prezzo()
                print(f"Prezzo totale: {locale.currency(totale, grouping=True)}")

        case 4:
            print(
                "Inserire [ 0 ] per annullare l'operazione."
                "\nInserire l'articolo da rimuovere\n"
                "es. 1, 2, 3..."
                  )
            indice = int(input(""))
            if indice == 0:
                continue
            while (indice < len(CARRELLO)) or (indice > len(CARRELLO)):
                print(f"L'articolo {indice} non esiste.")
                indice = int(input(""))
            
            CARRELLO.pop(indice - 1)
            print(f"\nL'articolo {indice} è stato rimosso.")

        case 5:
            print(
                "\nSei sicuro di voler CANCELLARE il carrello?\n"
            )
            conferma = input(" [s/n] ").lower()
            while (conferma != "s") and (conferma != "n"):
                print("L'input inserito non è valido. Riprova.\n")
                conferma = input("[ s/n ]").lower()
            
            if conferma == "n":
                continue

            CARRELLO.clear()
            print("\nCarrello svuotato.")

        case 6:
            indiceMax = 0
            costoMax = CARRELLO[0].prezzo()
            for i in range(1, len(CARRELLO)):
                if costoMax < CARRELLO[i].prezzo():
                    indiceMax = i
                    costoMax = CARRELLO[i].prezzo()
            print(f"\nL'articolo più costoso è {indiceMax} e costa {locale.currency(costoMax, grouping=True)}")

        case 8:
            CARRELLO.append(Sgabello(
                randint(3, 5),
                randint(1, 75),
                randint(10, 40),
                randint(1, 50)
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