# versione 0.0.5 del 16 Marzo 2026

from Memoria import *
import random

a = Memoria(5 , 3000 * 1000)  # max 5 elementi, max 30 secondi di vita

while True:
    print("[0] uscire")
    print("[1] inserire elemento da tastiera")
    print("[2] inserire elemento a random")
    print("[3] stampare conteggio")
    print("[4] stampare valori")
    print("[5] stampare Memoria")

    scelta = int(input("\nSCEGLI VOCE MENU : "))
    if scelta==0:
        break
    elif scelta==1:
        x = int(input("INSERISCI ELEMENTO : "))
        a.aggiungi(x)
    elif scelta==2:
        x = random.randint(10,99)
        a.aggiungi(x)
    elif scelta==3:
        print("ci sono " , a.conteggio() , "elementi")
    elif scelta==4:
        print("ci sono gli elementi" , a.elementi())
    elif scelta==5:
        print(a)
    print("------------------------------------")
        

print("PROGRAMMA TERMINATO")
