# Versione 0.1.3 del 02/03/2026

from Cassettiera import *
from Sgabello import *
from random import randint
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

scelta=-1
carrello=[]
x = True
while x:
    print("IKEA")
    print("------------------------------------")
    print("[0] Uscita")
    print("[1] Acquisto sgabello")
    print("[2] Acquisto cassettiera")
    print("[3] Stampa Carrello")
    print("[4] Svuota Carrello")
    print("[5] Acquisto sgabello random")
    print("[6] Acquisto cassettiera random")
    print("[7] Elimina un oggetto dal carrello")
    print("[8] Inserisci oggetto nel cassetto")
    print("------------------------------------")
    scelta = input("comando: ")
    ####################################
    
    if scelta == "0":
        break
    
    elif scelta == "1":
        a = int(input("Altezza: ")) #mettere vincoli
        ag = int(input("Altezza Gambe: "))
        ng = int(input("Numero Gambe: "))
        r = int(input("Raggio Seduta: "))
        try:
            s = Sgabello(ng,ag,r,a)
            carrello.append(s)
        except ValueError:
            print("Qualcosa è andato storto. Uno o più valori sono errati.")
        
    elif scelta == "2":
        nc = int(input("Numero Cassetti: "))
        m = input("Materiale: ")
        try: 
            c = Cassettiera(nc,m)
            carrello.append(c)
        except ValueError:
            print("Qualcosa è andato storto. Uno o più valori sono errati.")
        
        
    elif scelta == "3":
        ptot=0
        numOggetto = 0 
        for i in range(len(carrello)):
            p=carrello[i].prezzo()
            ptot+=p
            numOggetto += 1
            print("#"+str(numOggetto)+" "+str(carrello[i])+"\n")
        print("prezzo TOT "+str(locale.currency(ptot, grouping=True)))
        
    elif scelta == "4":
        conferma = input("Sei sicuro di voler svuotare il carrello? (s/n) ")
        if conferma.lower() == "s":
            carrello.clear()
            print("Svuotamento eseguito")
        elif conferma.lower() == "n": 
            print("Svuotamento annullato")
            
    elif scelta > "8" or scelta <"0":
        print("Comando non riconosciuto")
    
    elif scelta == "5":
        a = randint(10, 100)
        ag = randint(10, 100)
        ng = randint(3, 4)
        r = randint(20, 50)
        s = Sgabello(ng,ag,r,a)
        carrello.append(s)
        
    elif scelta == "6":
        nc = randint(2, 4)
        m = randint(1,2)
        if m == 1:
            m = "legno"
        elif m == 2:
            m = "plastica"
        c = Cassettiera(nc,m)
        carrello.append(c)
        
    elif scelta == "7":
        elimina_ogg = int(input("Quale oggetto vuoi eliminare dal carrello? "))
        if elimina_ogg > len(carrello) or elimina_ogg < 1:
            print("Oggetto inesistente.")
        else:
            carrello.pop(elimina_ogg-1)

    #elif scelta == "8":
     #   cassetto= self.
     #   cassetto = input("In che cassetto vuoi mettere l'oggetto: ")
     #   oggetto= input("inserisci un oggetto che vuoi mettere nel cassetto: ")
                       
                
        
print("PROGRAMMA TERMINATO")
