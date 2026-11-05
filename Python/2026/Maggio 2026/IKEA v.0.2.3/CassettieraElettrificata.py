from Cassettiera import *

class CassettieraElettrificata(Cassettiera):
    def __init__(self, nc, mat, voltaggio):
        super().__init__(nc, mat)  #RICHIAMO IL COSTRUTTORE DELLA SUPERCLASSE
        self.voltaggio = voltaggio
        self.statoLampadina = "spento"
    
    def __str__(self):
        s = super().__str__()
        s += " Voltaggio: "+str(self.voltaggio)+" Volt, "
        s += " Stato Lampadina: "+str(self.statoLampadina)
        return s

    def accendi(self):
        if self.statoLampadina == "Spento".lower():
            self.statoLampadina = "Acceso".lower()

    def spegni(self):
        if self.statoLampadina == "Acceso".lower():
            self.statoLampadina = "Spento".lower()