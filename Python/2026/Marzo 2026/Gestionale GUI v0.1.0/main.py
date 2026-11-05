import tkinter as t
from Sgabello import Sgabello
from Cassettiera import Cassettiera
from Domiciliari import Luca
from Luca import Malattie


class Menu:
    def __init__(self, colore: str, risoluzione: str, buttonWidth: int):
        self.versione = "0.1.0 del 30 Marzo 2026"
        self.finestra = t.Tk()
        self.finestra.title("Gestionale IKEA " + self.versione)
        self.finestra.config(bg=colore)
        self.finestra.geometry(risoluzione)
        self.finestra.resizable(False, False) #  x, y
        BUTTON_WIDTH = 20
        
        self.pulsanteA = t.Button(self.finestra, bg="red", width=BUTTON_WIDTH)
        self.pulsanteB = t.Button(self.finestra, bg="orange", width=BUTTON_WIDTH)
        self.pulsanteC = t.Button(self.finestra, bg="yellow", width=BUTTON_WIDTH)
        self.pulsanteD = t.Button(self.finestra, bg="green", width=BUTTON_WIDTH)
        self.pulsanteE = t.Button(self.finestra, bg="blue", width=BUTTON_WIDTH)
        self.pulsanteF = t.Button(self.finestra, bg="indigo", width=BUTTON_WIDTH)
        self.pulsanteG = t.Button(self.finestra, bg="violet", width=BUTTON_WIDTH)
        self.pulsanteH = t.Button(self.finestra, bg="black", width=BUTTON_WIDTH, command=self.finestra.destroy)

        self.etichettaA = t.Label(self.finestra, text="Acquisto sgabello")
        self.etichettaB = t.Label(self.finestra, text="Acquisto cassettiera")
        self.etichettaC = t.Label(self.finestra, text="Stampa carrello")
        self.etichettaD = t.Label(self.finestra, text="Svuota carrello")
        self.etichettaE = t.Label(self.finestra, text="Acquisto sgabello random")
        self.etichettaF = t.Label(self.finestra, text="Acquisto cassettiera random")
        self.etichettaG = t.Label(self.finestra, text="Elimina un oggetto dal carrello")
        self.etichettaH = t.Label(self.finestra, text="Esci")

        #self.pulsanteA.pack()
        #self.pulsanteB.pack()
        #self.pulsanteC.pack()
        #self.pulsanteD.pack()
        #self.pulsanteE.pack()
        #self.pulsanteF.pack()
        #self.pulsanteG.pack()

        #self.etichettaA.pack()
        #self.etichettaB.pack()
        #self.etichettaC.pack()
        #self.etichettaD.pack()
        #self.etichettaE.pack()
        #self.etichettaF.pack()
        #self.etichettaG.pack()

        self.pulsanteA.grid(row=0, column=0)
        self.pulsanteB.grid(row=1, column=0)
        self.pulsanteC.grid(row=2, column=0)
        self.pulsanteD.grid(row=3, column=0)
        self.pulsanteE.grid(row=4, column=0)
        self.pulsanteF.grid(row=5, column=0)
        self.pulsanteG.grid(row=6, column=0)
        self.pulsanteH.grid(row=7, column=0)

        self.etichettaA.grid(row=0, column=1, sticky="w")
        self.etichettaB.grid(row=1, column=1, sticky="w")
        self.etichettaC.grid(row=2, column=1, sticky="w")
        self.etichettaD.grid(row=3, column=1, sticky="w")
        self.etichettaE.grid(row=4, column=1, sticky="w")
        self.etichettaF.grid(row=5, column=1, sticky="w")
        self.etichettaG.grid(row=6, column=1, sticky="w")
        self.etichettaH.grid(row=7, column=1, sticky="w")
        

main = Menu("saddlebrown", "800x600")
t.mainloop()
