"""
Esercizio 1 – Conversione sicura
    Scrivi un programma che chieda all’utente di inserire un numero intero.
    Se l’utente non inserisce un numero valido, stampa "Non è un numero valido!".
    Se invece è valido, stampa il numero moltiplicato per 2.

Esercizio 2 – Divisione protetta
    Chiedi all’utente due numeri: dividendo e divisore.
    Se il divisore è zero, stampa "Non si può dividere per zero".
    Se uno dei valori non è un numero, stampa "Inserisci solo numeri".
    Altrimenti, stampa il risultato della divisione.

Esercizio 3 – Accesso sicuro a liste
    Hai la lista frutti = ["mela", "banana", "arancia"].
    Chiedi all’utente un indice e stampa l’elemento corrispondente.
    Se l’indice è fuori lista, stampa "Indice non valido".
    Se l’utente inserisce un valore non numerico, stampa "Inserisci un numero".

Esercizio 4 – Apertura file
    Prova ad aprire un file "dati.txt" e leggine il contenuto.
    Se il file non esiste, stampa "File non trovato".
    Usa finally per stampare "Operazione terminata" comunque.

Esercizio 5 – Multi-exception
    Scrivi un programma che:
    Chieda all’utente un numero intero.
    Provi a dividere 100 per quel numero.
    Gestisca sia ValueError (se l’input non è un numero) che ZeroDivisionError (se l’utente inserisce 0).
"""

def conversioneSciura():
    try:
        numero = int(input('Inserire un numero intero: '))
    except ValueError:
        print('Il numero inserito non é valido')
    else:
        print(numero*2)


def divisoneProtetta():
    try:
        dividendo = int(input('Inserire il dividendo: '))
        divisore = int(input('Inserire il divisore: '))
        print(dividendo / divisore)
    except ValueError:
        print('Dividendo e divisore devono essere numeri.')
    except ZeroDivisionError:
        print('Il divisore non puó essere 0.')
    # else:
    #    print(dividendo / divisore)
    # Se la else scatena l'errore, non controlla le eccezioni.
divisoneProtetta()
