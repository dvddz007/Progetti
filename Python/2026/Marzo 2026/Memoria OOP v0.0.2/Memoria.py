import time

class Memoria:
    def __init__(self, nMax: int, tMaxMS: int | float):
        self.nMax = nMax
        self.tMax = tMaxMS
        self.valori = []

    def __str__(self):
        s = f"nMax: {self.nMax} tMax: {self.tMax}ms \nvalori: \n{self.valori}\nSomma: {self.somma()}"
        if self.valori:
            s += f"Media: {self.media()}" 
        return s
    
    def svecchia(self) -> None:
        '''
            Il tempo è basato sul UTS (UNIX Time Stamp).
        '''
        tNow = time.time() * 1000 #  inizio il timer in ms
        if len(self.valori) > 0:
            fai=True
            while fai:
                #  se la differenza tra l'UTS di adesso e l'UTS precedente è maggiore di tMax
                if (tNow - self.valori[0][1]) > self.tMax:
                    self.valori.pop(0)
                    fai = len(self.valori) > 0
                else:
                    fai = False
        
        #  rimuovo il valore più vecchio SE ho raggiunto nMax valori salvati
        while len(self.valori) >= self.nMax:
            self.valori.pop(0)


    def aggiungi(self, valore: int | float) -> None:
        #  aggiunge il valore e il tempo in cui è stato aggiunto come tupla
        self.valori.append(tuple([valore, time.time()]))
        return

    def somma(self) -> int | float:
        if not self.valori:
            return 0

        somma = 0
        for i in range(len(self.valori)):
            somma += self.valori[i][0]
        return somma

    def media(self) -> int | float:
        # 0 / 0 da ZeroDivisionError
        if not self.valori:
            return 0
        
        self.svecchia()
        return self.somma() / len(self.valori)
    
    def eta(self):
        """
            Restituisce la differenza di tempo tra l'ultimo e il primo tempo registrati.
        """
        return self.valori[-1][1] - self.valori[0][1]
