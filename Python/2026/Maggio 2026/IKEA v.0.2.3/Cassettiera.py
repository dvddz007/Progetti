#versione 0.2.1 del 22/04/2026

import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

class Cassettiera:
    materiali = ["plastica", "acciaio" , "vetro" , "legno"]

    def __init__(self, nc, m):

        # validazione parametri costruttore
        if nc<=1 or nc>=10:
            raise ValueError ("impossibile creare una cassettiera con",nc,"cassetti")
        if not m in self.materiali:
            raise ValueError ("impossibile creare una cassettiera di",m)

        # ok, i parametri sono validi, li memorizzo negli attributi
        self.numeroCassetti = nc
        self.cassetti = [""]*nc
        self.materiale = m
        
    def __str__(self):
        stampa = "numero cassetti: " + str(self.numeroCassetti)
        stampa += ", materiale: " + str(self.materiale)
#        stampa += ", contenuto cassetti: " + str(self.cassetti)
        stampa += ", prezzo " + str(locale.currency(self.prezzo(), grouping=True))
        
        return stampa

    def aggiungi(self, ogg, cass):
        if cass > self.numeroCassetti or cass <= 0:
            raise ValueError("Il cassetto scelto non esiste.")
        elif self.cassetti[cass-1] != "":
            raise ValueError("Il cassetto è pieno.")
        elif ogg == "" or ogg == None:
            raise ValueError("Non si può inserire un oggetto vuoto.")
        self.cassetti[cass-1] = ogg

    def rimuovi(self, cass):
        if self.cassetti[cass-1] != "":
            self.cassetti[cass-1] = ""
        else:
            raise ValueError("Il cassetto è già vuoto, impossibile svuotarlo.")

    def prezzo(self):
        i = 1 + self.materiali.index(self.materiale)
        return i * self.numeroCassetti
    
        
        
        
