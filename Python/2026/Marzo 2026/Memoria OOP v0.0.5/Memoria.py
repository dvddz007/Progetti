#versione 0.0.5 del 16/03/2026

import time

class Memoria:
    def __init__(self, nMax, tMaxMS):
        self.nMax       = nMax
        self.tMaxMS     = tMaxMS
        self.valori     = []
        self.birthTime  = int(time.time() * 1000)

    def __str__(self):
        self.svecchia() # aggiunto il 9 Marzo alle 12.15 dal prof

        s=""
#        s+= "nMax: " + str(self.nMax) + "\n"
#        s+= "tMaxMS: " + str(self.tMaxMS) + "\n"
#        s+= "Età: " + str(self.eta()) + "\n"
        s+= "Conteggio: " + str(self.conteggio()) + "\n"
        s+= "Somma: " + str(self.somma()) + "\n"
        if self.conteggio() > 0:
            s+= "Media: " + str(self.media()) + "\n"
        s+= "Valori: " + str(self.valori) + "\n"
        s+= "Tempo attuale: " + str(int(time.time() * 1000) - self.birthTime) + "\n"
        return s

    def svecchia(self):
        tNow = int(time.time()*1000) - self.birthTime # time elapsed since birth
        if len(self.valori) > 0:
            fai=True
            while fai:
                if tNow - self.valori[0][1] > self.tMaxMS:
                    self.valori.pop(0)
                    print("#",end="")
                    fai = (len(self.valori) > 0)
                else:
                    fai = False

        n = len(self.valori) 
        while n > self.nMax:
            self.valori.pop(0)
            n = len(self.valori) 
            print("*",end="")

    def aggiungi(self, valore):
        tNow = int(time.time() * 1000) - self.birthTime # aggiunto dalla classe il 16/03/2026

        #https://www.geeksforgeeks.org/python/tuple-constructor-in-python/
        self.valori.append(tuple([valore, tNow]))
        self.svecchia()

    def somma(self):
        self.svecchia()
        somma=0
        for n in self.valori:
            somma += n[0]
        return somma

    def media(self):
#        self.svecchia() non serve chiamarlo,
#                        perchè lo chiamo alla riga dopo
        media = self.somma()
        media /= len(self.valori)
        return media
    
    def eta(self):
        if len(self.valori) > 0:
            self.svecchia()
            n = len(self.valori)
            youngest= self.valori[n-1][1]
            oldest  = self.valori[0][1]
            diff = youngest - oldest
            return diff
        return -1

    def conteggio(self):
        self.svecchia()
        return len(self.valori)

    def elementi(self):
        self.svecchia()
        s=""
        for n in self.valori:
            s += str(n[0])+","
        return s
