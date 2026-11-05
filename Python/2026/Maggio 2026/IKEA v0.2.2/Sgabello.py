#versione 0.0.6 del 23/04/2026
from math import pi

import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

class Sgabello:
    
    def __init__(self, ng, ag, r, a):
    #di seguito ci sono i 4 attributi,cio che l oggetto è o ha:
        if ng <= 2:
            raise ValueError("Numero gambe errato. (Devono essere almeno 3.)")
        self.numeroGambe=ng
        
        if ag < 10:
            raise ValueError("Altezza gambe errata. (Devono essere alte almeno 10 cm.)")
        self.altezzaGambe=ag
        
        if r <= 15:
            raise ValueError("Raggio della seduta errato. (Deve essere almeno 15 cm.)")
        self.raggioSeduta=r

        if a <= 2:
            raise ValueError("Altezza seduta errata. (Deve essere alta almeno 2 cm.)")
        self.altezzaSeduta=a
        
    def __str__(self):

        s="lo sgabello ha "+ str(self.numeroGambe)+" gambe,"
        s+=" l'altezza delle gambe è di: " +str(self.altezzaGambe)+" cm,"
        s+=" il raggio della seduta è di: " + str(self.raggioSeduta)+" cm"
        s+=" mentre l'altezza della seduta è di: " + str(self.altezzaSeduta)+" cm"
        s+=" il prezzo dello sgabello è di: " + str(locale.currency(self.prezzo(), grouping=True))
        return s
    
    def aggiungiGamba(self):
        #self.numeroGambe+=1
        self.aggiungiGambe(1)
        
    def aggiungiGambe(self, ng):
        if (self.numeroGambe+ng) < 3:
            raise ValueError("Numero di gambe errato. (Devono essere almeno 3.)")
        self.numeroGambe+=ng

    def volume(self):
        return pi * self.raggioSeduta**2 * self.altezzaSeduta

    def prezzo(self):
        #lo sgabello costa 0.00023 euro al cm cubo della seduta + 5 euro per gamba
        prezzoSeduta = self.volume()*0.00023
        prezzoGambe = self.numeroGambe*5
        return round(prezzoSeduta + prezzoGambe,2)
