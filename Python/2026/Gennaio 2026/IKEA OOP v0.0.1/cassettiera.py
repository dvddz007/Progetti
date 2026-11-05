class Cassettiera:
    def __init__(self, nc: int): #  metodo costruttore
        '''
            nc: numero cassetti.
        '''
        #  attributi degli oggetti. possono essere chiamati come metodo.
        self.numeroCassetti = nc
        self.primoCassetto = None
        self.secondoCassetto = None
        self.terzoCassetto = None


    def __str__(self): #  metodo conversione in stringa
        '''
            Restituisce SEMPRE una stringa.
        '''
        s = "Contenuto della cassettiera:\n"
        if self.primoCassetto != None:
            s += f"Il primo cassetto contiene: {self.primoCassetto}\n"
        if self.secondoCassetto != None:
            s += f"Il secondo cassetto contiene: {self.secondoCassetto}\n"
        if self.numeroCassetti > 2:
            if self.terzoCassetto != None:
                s += f"Il terzo cassetto contiene: {self.terzoCassetto}\n"
        return s


    def aggiungiCassetto(self, cassetto: int, oggetto: str):
        #  validazione dei dati
        if (oggetto == "") or (oggetto == None) or (not isinstance(oggetto, str)):
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
