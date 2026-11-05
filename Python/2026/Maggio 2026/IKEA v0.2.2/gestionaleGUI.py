#ZONA IMPORT ############################################################
from Cassettiera import *
from Sgabello import *
import tkinter as t
from tkinter import ttk

#ZONA COSTANTI ##########################################################
LARGHEZZA_PULSANTE = 20

class gestionaleGUI:

    def stampaCarrello(self):
        print("STAMPA CARRELLO")
        
        if len(self.carrello) == 0:
            self.listaCarrello.insert(1,"Carrello vuoto.")
        else:
            for i in range(len(self.carrello)):
                a=str(self.carrello[i])
                self.listaCarrello.insert(1,a)
                
    
    def svuotaCarrello(self):
        print("SVUOTA CARRELLO")
        self.carrello.clear()
        self.stampaCarrello()
        
    def acquistoCassettiera(self,nc,m):
        print("acquisto una cassettiera di",nc,"cassetti fatta in",m)
        x = Cassettiera(int(nc),m)
        self.carrello.append(x)
        self.stampaCarrello()

    def acquistoSgabello(self,ng, ag, r, a):
        print("acquisto uno sgabello con", ng, "gambe di altezza", ag, "e raggio", r, "con altezza seduta", a)
        x = Sgabello(int(ng), float(ag), float(r), float(a))
        self.carrello.append(x)
        self.stampaCarrello()

    def aggiungiCarrello(self, oggetto):
        self.carrello.append(oggetto)
        self.listaCarrello.insert(t.END,str(oggetto))
        s = "è stato aggiunto "
        if isinstance(oggetto, Cassettiera):
            s += "Cassettiera"
        elif isinstance(oggetto, Sgabello):
            s += "Sgabello"
        s += " al carrello"
        print(s)
        return

    
    def addMassimo(self, carrello):
        if not carrello:
            self.listaCarrello.insert(t.END, 'Il carrello é vuoto')
            return
        massimo = carrello[0]
        for articolo in carrello:
            if articolo.prezzo() > massimo.prezzo():
                massimo = articolo
        self.listaCarrello.insert(t.END, f'Articolo piú costoso: {massimo}')
        return


    def addMedia(self, carrello):
        if not carrello:
            self.etichettaMedia.config(text='Prezzo medio: carrello vuoto')
            return
        medio = (sum([articolo.prezzo() for articolo in carrello])) / len(carrello)
        self.etichettaMedia.config(text=f'Prezzo medio: {round(medio, 2)}')
        return


    def addConta(self, carrello):
        if not carrello:
            self.listaCarrello.insert(t.END, 'Il carrello é vuoto')
            return
        self.listaCarrello.insert(t.END, f'Numero articoli: {len(carrello)}')
        return


    def finestraAcquistoSgabello(self):
        f = t.Tk()
        f.title("Acquisto Sgabello")
        f.config(bg = "red")
        f.geometry ("320x200")
        f.resizable(False, False)
        # dovrei nascondere la FINESTRA MADRE

        # prima riga : NUMERO GAMBE
        etichetta1 = t.Label(f, text="Numero gambe")
        etichetta1.grid(row=0 , column=0 )
        # Creazione della Combobox
        opzioni = []
        for i in range(3, 5):
            opzioni.append(str(i))
        cmb1 = ttk.Combobox(f, values=opzioni, state="readonly")
        cmb1.set("Quante gambe?") # Testo predefinito
        cmb1.grid(row=0 , column=1 )

        # seconda riga : ALTEZZA
        name_var = ""
        etichetta2 = t.Label(f, text="Altezza gambe")
        etichetta2.grid(row=1 , column=0 )
        # Creazione della Combobox
        ent2 = t.Entry(f, textvariable = name_var, font=('calibre',10,'normal'))
        ent2.grid(row=1 , column=1 )

        # terza riga : Raggio
        etichetta3 = t.Label(f, text="Raggio sgabello")
        etichetta3.grid(row=2 , column=0 )
        ent3 = t.Entry(f, textvariable = name_var, font=('calibre',10,'normal'))
        ent3.grid(row=2 , column=1 )

        # quarta riga : Altezza seduta
        etichetta4 = t.Label(f, text="Altezza seduta")
        etichetta4.grid(row=3 , column=0 )
        ent4 = t.Entry(f, textvariable = name_var, font=('calibre',10,'normal'))
        ent4.grid(row=3 , column=1 )

        # pulsanti aggiungi/annulla
        pulsante7 = t.Button(f ,bg="white" ,
                                text="Aggiungi al carrello",
                                width=LARGHEZZA_PULSANTE,
                                command=lambda: self.aggiungiCarrello(Sgabello(
                                    int(cmb1.get()),
                                    float(ent2.get()),
                                    float(ent3.get()),
                                    float(ent4.get()))
                                ))
        pulsante8 = t.Button(f ,bg="black" ,
                                fg="white",
                                text="Esci",
                                width=LARGHEZZA_PULSANTE,
                                command=f.destroy)
        pulsante7.grid(row=4, column=0)
        pulsante8.grid(row=4, column=1)

        f.mainloop()

    def finestraAcquistoCassettiera(self):
        f = t.Tk()
        f.title("Acquisto Cassettiera")
        f.config(bg = "orange")
        f.geometry ("320x200")
        f.resizable(False, False)
        # dovrei nascondere la FINESTRA MADRE

        # prima riga : NUMERO CASSETTI
        etichetta1 = t.Label(f, text="numero cassetti")
        etichetta1.grid(row=0 , column=0 )
        # Creazione della Combobox
        opzioni = []
        for i in range(2,10):
            opzioni.append(str(i))
        cmb1 = ttk.Combobox(f, values=opzioni, state="readonly")
        cmb1.set("Quanti cassetti?") # Testo predefinito
        cmb1.grid(row=0 , column=1 )

        # seconda riga : MATERIALE
        etichetta2 = t.Label(f, text="materiale")
        etichetta2.grid(row=1 , column=0 )
        # Creazione della Combobox
        opzioni = ["legno","plastica","vetro","acciaio"]
        cmb2 = ttk.Combobox(f, values=opzioni, state="readonly")
        cmb2.set("Quale materiale?") # Testo predefinito
        cmb2.grid(row=1 , column=1 )

        # pulsanti aggiungi/annulla
        pulsante7 = t.Button(f ,bg="white" ,
                                text="Aggiungi al carrello",
                                width=LARGHEZZA_PULSANTE,
                                command=lambda: self.aggiungiCarrello(Cassettiera(
                                    int(cmb1.get()),
                                    str(cmb2.get()))
                                ))
        pulsante8 = t.Button(f ,bg="black" ,
                                fg="white",
                                text="Esci",
                                width=LARGHEZZA_PULSANTE,
                                command=f.destroy)
        pulsante7.grid(row=2 , column=0)
        pulsante8.grid(row=2 , column=1)

        f.mainloop()    
        
    def __init__(self):
        self.versione="0.2.2 del 23 aprile 2026"
        self.carrello = []
        self.finestra = t.Tk()
        self.finestra.title("Gestionale IKEA "+self.versione)
        self.finestra.config(bg = "brown")
        self.finestra.geometry ("800x600")
        self.finestra.resizable(False, False)
        self.listaCarrello = t.Listbox(self.finestra, height = 10, 
                                    width = 75, 
                                    bg = "whitesmoke",
                                    activestyle = 'dotbox',
                                    fg = "darkblue")
        self.tot=t.Label()
        self.listaCarrello.grid(row=17 , column=22)
        
        self.pulsante1 = t.Button(self.finestra ,bg="red" , width=LARGHEZZA_PULSANTE,
                                  command=self.finestraAcquistoSgabello)
        self.etichetta1 = t.Label(self.finestra, text="Acquisto sgabello")
        
        self.pulsante1.grid(row=0 , column=0, )
        self.etichetta1.grid(row=0 , column=1,sticky="w")


        self.pulsante2 = t.Button(self.finestra ,   bg="orange" ,
                                                  width=LARGHEZZA_PULSANTE,
                                                  command=self.finestraAcquistoCassettiera)
        self.etichetta2 = t.Label(self.finestra, text="Acquisto cassettiera")
        
        self.pulsante2.grid(row=1 , column=0)
        self.etichetta2.grid(row=1 , column=1, sticky="w")

        self.pulsante2 = t.Button(self.finestra ,   bg="orange" ,
                                                  width=LARGHEZZA_PULSANTE,
                                                  command=self.finestraAcquistoCassettiera)
        self.etichetta2 = t.Label(self.finestra, text="Acquisto cassettiera")

        self.pulsante3 = t.Button(self.finestra ,bg="yellow" , width=LARGHEZZA_PULSANTE,
                                  command=self.stampaCarrello)
        self.etichetta3 = t.Label(self.finestra, text="Stampa carrello")
        self.pulsante3.grid(row=2 , column=0)
        self.etichetta3.grid(row=2 , column=1, sticky="w")

        self.pulsante4 = t.Button(self.finestra ,bg="green" , width=LARGHEZZA_PULSANTE,command=self.svuotaCarrello)
        self.etichetta4 = t.Label(self.finestra, text="Svuota carrello")
        self.pulsante4.grid(row=4 , column=0)
        self.etichetta4.grid(row=4 , column=1, sticky="w")

        self.pulsante5 = t.Button(self.finestra ,bg="blue" , width=LARGHEZZA_PULSANTE)
        self.etichetta5 = t.Label(self.finestra, text="Acquisto sgabello random")
        self.pulsante5.grid(row=5 , column=0)
        self.etichetta5.grid(row=5 , column=1, sticky="w")

        self.pulsante6 = t.Button(self.finestra ,bg="indigo" , width=LARGHEZZA_PULSANTE)
        self.etichetta6 = t.Label(self.finestra, text="Acquisto cassettiera random")
        self.pulsante6.grid(row=6 , column=0)
        self.etichetta6.grid(row=6 , column=1, sticky="w")
        
        self.pulsante7 = t.Button(self.finestra ,bg="violet" , width=LARGHEZZA_PULSANTE)
        self.etichetta7 = t.Label(self.finestra, text="Elimina un oggetto dal carrello")
        self.pulsante7.grid(row=7 , column=0)
        self.etichetta7.grid(row=7 , column=1, sticky="w")

        self.pulsante9 = t.Button(self.finestra ,bg="white" , width=LARGHEZZA_PULSANTE, command=lambda: self.addMassimo(self.carrello))
        self.etichetta9 = t.Label(self.finestra, text="Trova oggetto piú costoso")
        self.pulsante9.grid(row=8 , column=0)
        self.etichetta9.grid(row=8 , column=1, sticky="w")

        self.pulsante10 = t.Button(self.finestra ,bg="white" , width=LARGHEZZA_PULSANTE, command=lambda: self.addMedia(self.carrello))
        self.etichetta10 = t.Label(self.finestra, text="Prezzo medio del carrello")
        self.pulsante10.grid(row=9 , column=0)
        self.etichetta10.grid(row=9 , column=1, sticky="w")

        self.pulsante11 = t.Button(self.finestra ,bg="white" , width=LARGHEZZA_PULSANTE, command=lambda: self.addConta(self.carrello))
        self.etichetta11 = t.Label(self.finestra, text="Conta oggetti nel carrello")
        self.pulsante11.grid(row=10 , column=0)
        self.etichetta11.grid(row=10 , column=1, sticky="w")

        self.pulsante8 = t.Button(self.finestra , bg="black" ,
                                                  width=LARGHEZZA_PULSANTE,
                                                  command=self.finestra.quit)
        self.etichetta8 = t.Label(self.finestra, text="Uscita")
        self.pulsante8.grid(row=15 , column=0)
        self.etichetta8.grid(row=15 , column=1, sticky="W")

        self.etichettaMedia = t.Label(self.finestra, text="Prezzo medio: -")
        self.etichettaMedia.grid(row=16, column=22)
        t.mainloop()

### MAIN
main = gestionaleGUI()
