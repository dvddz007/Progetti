class Sgabello:
    def __init__(self, numeroGambe: int, altezzaGambe: int, raggio: float, altezza: float):
        self.numeroGambe = numeroGambe
        self.altezzaGambe = altezzaGambe
        self.raggio = raggio
        self.altezza = altezza

    
    def __str__(self):
        if self.numeroGambe < 3:
            return "Sgabello impossibile"
        s =  f"Lo sgabello ha {self.numeroGambe} gambe di altezza {self.altezzaGambe} cm. "
        s += f"Il suo raggio è di {self.raggio} cm e la sua altezza è {self.altezza} cm."
        return s 
    

    def aggiungiGamba(self):
        self.numeroGambe += 1


    def aggiungiGambe(self, gambeAggiunte: int):
        self.numeroGambe += gambeAggiunte
