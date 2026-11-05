from math import pi
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


class Cassettiera:
    def __init__(self, nc: int, materiale: str): #  metodo costruttore
        '''
            nc: numero cassetti.
        '''
        #  attributi degli oggetti. possono essere chiamati come metodo.
        if nc < 2 or nc > 3:
            raise ValueError("Il numero di cassetti deve essere compreso tra 1 e 3.")
        
        materiale = materiale.lower()
        if materiale not in ["legno", "plastica", "acciaio"]:
            raise ValueError("Il materiale deve essere 'legno', 'plastica' o 'acciaio'.")
        
        self.numeroCassetti = nc
        self.primoCassetto = None
        self.secondoCassetto = None
        self.terzoCassetto = None
        self.materiale = materiale


    def __str__(self): #  metodo conversione in stringa
        '''
            Restituisce SEMPRE una stringa.
        '''

        s = ""

        if (self.primoCassetto is None and
            self.secondoCassetto is None and
            self.terzoCassetto is None):
            return f"Cassettiera vuota di {self.materiale}."

        s = "Contenuto della cassettiera:\n"

        if self.primoCassetto is not None:
            s += f"Il primo cassetto contiene: {self.primoCassetto}\n"

        if self.secondoCassetto is not None:
            s += f"Il secondo cassetto contiene: {self.secondoCassetto}\n"

        if self.numeroCassetti == 3 and self.terzoCassetto is not None:
            s += f"Il terzo cassetto contiene: {self.terzoCassetto}\n"

        s += f"Materiale: {self.materiale}\n"
        s += f"Prezzo: {locale.currency(self.prezzo(), grouping=True)}"

        return s


    def aggiungiCassetto(self, cassetto: int, oggetto: str):
        #  validazione dei dati
        if not isinstance(oggetto, str):
            raise ValueError("L'oggetto inserito deve essere una stringa.")
        
        if (oggetto == "") or (oggetto == None):
            raise ValueError("Oggetto mancante. Impossibile inserire.")
        
        if (cassetto < 1) or (cassetto > self.numeroCassetti):
            raise ValueError("Cassetto inesistente. Impossibile inserire.")
        
        if cassetto == 1:
            self.primoCassetto = oggetto
        elif cassetto == 2:
            self.secondoCassetto = oggetto
        else:
            self.terzoCassetto = oggetto
        return


    def prezzo(self):
        if self.materiale == "legno":
            return self.numeroCassetti * 15
        if self.materiale == "acciaio":
            return self.numeroCassetti * 12
        if self.materiale == "plastica":
            return self.numeroCassetti * 11.5
        raise ValueError(f"Il materiale '{self.materiale}' non è valido.")
    