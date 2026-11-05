from math import pi
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


class Sgabello:
    def __init__(self, numeroGambe: int, altezzaGambe: int, raggio: float, altezza: float):
        self.numeroGambe = numeroGambe
        self.altezzaGambe = altezzaGambe
        self.raggio = raggio
        self.altezza = altezza

    
    def __str__(self):
        if self.numeroGambe < 3:
            return "Sgabello impossibile\n"
        return f"Lo sgabello ha {self.numeroGambe} gambe di altezza {self.altezzaGambe} cm. Il suo raggio è di {self.raggio} cm. La sua altezza è {self.altezza} cm."
    

    def aggiungiGamba(self):
        self.numeroGambe += 1


    def aggiungiGambe(self, gambeAggiunte: int):
        self.numeroGambe += gambeAggiunte


    def volume(self):
        return pi * (self.raggio**2 * self.altezza)

    def prezzo(self):
        #  lo sgabello costa 0.00023 euro al cm cubo della seduta + 5 euro per gamba
        prezzoSeduta = self.volume() * 0.00023
        prezzoGambe = self.numeroGambe*5
        return round(prezzoSeduta + prezzoGambe, 2)
