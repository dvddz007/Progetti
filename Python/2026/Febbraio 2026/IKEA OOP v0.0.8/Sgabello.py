from math import pi
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


class Sgabello:
    def __init__(self, numeroGambe: int, altezzaGambe: int, raggio: float, altezza: float):
        if numeroGambe < 3:
            raise ValueError("Il numero di gambe deve essere almeno 3.")
        if altezzaGambe < 10:
            raise ValueError("L'altezza delle gambe deve essere almeno 10.")
        if raggio < 50:
            raise ValueError("Il raggio deve essere almeno 50.")
        if altezza < 100:
            raise ValueError("L'altezza della seduta deve essere almeno 100.")
        
        self.numeroGambe = numeroGambe
        self.altezzaGambe = altezzaGambe
        self.raggio = raggio
        self.altezza = altezza

    
    def __str__(self):
        return f"Lo sgabello ha {self.numeroGambe} gambe di altezza {self.altezzaGambe} cm. Il suo raggio è di {self.raggio} cm. La sua altezza è {self.altezza} cm."
    

    def aggiungiGamba(self) -> None:
        self.numeroGambe(1)


    def aggiungiGambe(self, gambeAggiunte: int) -> None:
        if (self.numeroGambe + gambeAggiunte) < 3:
            raise ValueError("Numero di gambe errato. Deve essere almeno 3.")
        self.numeroGambe += gambeAggiunte


    def volume(self) -> int:
        return pi * (self.raggio**2 * self.altezza)


    def prezzo(self) -> int:
        #  lo sgabello costa 0.00023 euro al cm cubo della seduta + 5 euro per gamba
        prezzoSeduta = self.volume() * 0.00023
        prezzoGambe = self.numeroGambe*5
        return round(prezzoSeduta + prezzoGambe, 2)
