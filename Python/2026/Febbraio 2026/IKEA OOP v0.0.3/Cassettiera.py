from math import pi
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


class Cassettiera:
    def __init__(self, nc: int, materiale: str): #  metodo costruttore
        '''
            nc: numero cassetti.
        '''
        #  attributi degli oggetti. possono essere chiamati come metodo.
        self.numeroCassetti = nc
        self.primoCassetto = None
        self.secondoCassetto = None
        self.terzoCassetto = None
        self.materiale = materiale.lower()


    def __str__(self): #  metodo conversione in stringa
        '''
            Restituisce SEMPRE una stringa.
        '''
        s = "Contenuto della cassettiera:\n"
        if self.primoCassetto != None:
            s += f"Il primo cassetto contiene: {self.primoCassetto}. Il materiale usato è {self.materiale}. Il suo costo è: {self.prezzo()}\n"
        if self.secondoCassetto != None:
            s += f"Il secondo cassetto contiene: {self.secondoCassetto}. Il materiale usato è {self.materiale}. Il suo costo è: {self.prezzo()}\n"
        if self.numeroCassetti > 2:
            if self.terzoCassetto != None:
                s += f"Il terzo cassetto contiene: {self.terzoCassetto}. Il materiale usato è {self.materiale}. Il suo costo è: {self.prezzo()}\n"
        return s


    def aggiungiCassetto(self, cassetto: int, oggetto: str):
        #  validazione dei dati
        if not isinstance(oggetto, str):
            print("L'oggetto inserito deve essere una stringa.")
            return
        if (oggetto == "") or (oggetto == None):
            print("Oggetto mancante. Impossibile inserire.")
            return
        if (cassetto < 1) or (cassetto > self.numeroCassetti):
            print("Cassetto inesistente. Impossibile inserire.")
            return
        
        if cassetto == 1:
            self.primoCassetto = oggetto
        elif cassetto == 2:
            self.secondoCassetto = oggetto
        else:
            self.terzoCassetto = oggetto
        return


    def prezzo(self):
        if self.materiale == "legno":
            return f"{locale.currency(self.numeroCassetti * 15, grouping=True)}"
        if self.materiale == "plastica":
            return f"{locale.currency(self.numeroCassetti * 11.5, grouping=True)}"
        print(f"Il materiale '{self.materiale}' non è valido.")
        return
    