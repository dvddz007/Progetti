# ZONA IMPORT ############################################################
from Cassettiera import *
from Sgabello import *
from CassettieraElettrificata import *
import tkinter as t
from tkinter import ttk
import random

# ZONA COSTANTI ##########################################################
LARGHEZZA_PULSANTE = 20


class gestionaleGUI:

    # -------------------------------------------------
    def calcolaTotale(self):
        totale = 0
        for oggetto in self.carrello:
            totale += oggetto.prezzo()
        return totale

    # -------------------------------------------------
    
    def aggiornaGui(self):
        self.listaCarrello.delete(0, t.END)

        if len(self.carrello) == 0:
            self.listaCarrello.insert(t.END, "Carrello vuoto")
        else:
            for i in range(len(self.carrello)):
                oggetto = self.carrello[i]
                testo = str(i+1) + ") " + str(oggetto)
                self.listaCarrello.insert(t.END, testo)

        # aggiorna totale
        totale = self.calcolaTotale()
        self.labelTotale.config(text="Totale: " + str(totale) + " €")

    def stampaCarrello(self):
        self.aggiornaGui()
    # -------------------------------------------------
    def svuotaCarrello(self):
        print("SVUOTA CARRELLO")
        self.carrello.clear()
        self.stampaCarrello()

    # -------------------------------------------------
    def acquistoCassettiera(self, nc, m, elettrica=False):
        print("acquisto cassettiera:", nc, m)
        try:
            if elettrica:
                x = CassettieraElettrificata(int(nc), m)
                self.carrello.append(x)
                self.stampaCarrello()
            else:
                x = Cassettiera(int(nc), m)
                self.carrello.append(x)
                self.stampaCarrello()
        except:
            print("Errore nei dati")
        

    # -------------------------------------------------
    def acquistoSgabello(self, ng, ag, r, a):
        print("acquisto sgabello:", ng, ag, r, a)
        try:
            s = Sgabello(int(ng), int(ag), int(r), int(a))
            self.carrello.append(s)
            self.stampaCarrello()
        except:
            print("Errore nei dati")

    # -------------------------------------------------
    def acquistoSgabelloRandom(self):
        print("sgabello random")
        ng = random.choice([3, 4])
        ag = random.randint(30, 100)
        r = random.choice([20, 30, 40, 50])
        a = random.randint(30, 100)

        s = Sgabello(ng, ag, r, a)
        self.carrello.append(s)
        self.stampaCarrello()

    # -------------------------------------------------
    def acquistoCassettieraRandom(self):
        print("cassettiera random")
        nc = random.randint(2, 9)
        materiali = ["legno", "plastica", "vetro", "acciaio"]
        m = random.choice(materiali)

        c = Cassettiera(nc, m)
        self.carrello.append(c)
        self.stampaCarrello()

    # -------------------------------------------------
    def finestraAcquistoSgabello(self):
        f = t.Toplevel(self.finestra)
        f.title("Acquisto Sgabello")
        f.config(bg="lightblue")
        f.geometry("350x250")
        f.resizable(False, False)

        t.Label(f, text="numero gambe").grid(row=0, column=0)
        cmb_ng = ttk.Combobox(f, values=["3", "4"], state="readonly")
        cmb_ng.set("Quante gambe?")
        cmb_ng.grid(row=0, column=1)

        t.Label(f, text="altezza gambe").grid(row=1, column=0)
        entry_ag = t.Entry(f)
        entry_ag.grid(row=1, column=1)

        t.Label(f, text="raggio seduta").grid(row=2, column=0)
        cmb_r = ttk.Combobox(f, values=["20", "30", "40", "50"], state="readonly")
        cmb_r.set("Raggio?")
        cmb_r.grid(row=2, column=1)

        t.Label(f, text="altezza seduta").grid(row=3, column=0)
        entry_a = t.Entry(f)
        entry_a.grid(row=3, column=1)

        t.Button(f, text="Acquista", width=LARGHEZZA_PULSANTE,
                 command=lambda: self.acquistoSgabello(
                     cmb_ng.get(), entry_ag.get(), cmb_r.get(), entry_a.get()
                 )).grid(row=4, column=0)

        t.Button(f, text="Annulla", width=LARGHEZZA_PULSANTE,
                 command=f.destroy).grid(row=4, column=1)

    # -------------------------------------------------
    def finestraAcquistoCassettiera(self):
        f = t.Toplevel(self.finestra)
        f.title("Acquisto Cassettiera")
        f.config(bg="orange")
        f.geometry("320x200")
        f.resizable(False, False)

        t.Label(f, text="numero cassetti").grid(row=0, column=0)

        opzioni = []
        for i in range(2, 10):
            opzioni.append(str(i))

        cmb1 = ttk.Combobox(f, values=opzioni, state="readonly")
        cmb1.set("Quanti cassetti?")
        cmb1.grid(row=0, column=1)

        t.Label(f, text="materiale").grid(row=1, column=0)

        opzioni = ["legno", "plastica", "vetro", "acciaio"]
        cmb2 = ttk.Combobox(f, values=opzioni, state="readonly")
        cmb2.set("Quale materiale?")
        cmb2.grid(row=1, column=1)

        t.Label(f, text="Elettrica").grid(row=2, column=0)

        checkBoxElettrica = t.Checkbutton(f, text="")
        checkBoxElettrica.grid(row=2, column=1)

        t.Button(f, bg="white",
                 text="Acquista",
                 width=LARGHEZZA_PULSANTE,
                 command=lambda: self.acquistoCassettiera(
                     cmb1.get(), cmb2.get()
                 )).grid(row=3, column=0)

        t.Button(f, bg="black", fg="white",
                 text="Esci",
                 width=LARGHEZZA_PULSANTE,
                 command=f.destroy).grid(row=3, column=1)

    # -------------------------------------------------

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
    

    def __init__(self):
        self.versione = "0.2.3"
        self.carrello = []

        self.finestra = t.Tk()
        self.finestra.title("Gestionale IKEA " + self.versione)
        self.finestra.config(bg="brown")
        self.finestra.geometry("800x600")
        self.finestra.resizable(False, False)

        self.pulsante1 = t.Button(self.finestra, bg="red",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.finestraAcquistoSgabello)
        self.etichetta1 = t.Label(self.finestra, text="Acquisto sgabello")
        self.pulsante1.grid(row=0, column=0)
        self.etichetta1.grid(row=0, column=1, sticky="w")

        self.pulsante2 = t.Button(self.finestra, bg="orange",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.finestraAcquistoCassettiera)
        self.etichetta2 = t.Label(self.finestra, text="Acquisto cassettiera")
        self.pulsante2.grid(row=1, column=0)
        self.etichetta2.grid(row=1, column=1, sticky="w")

        self.pulsante3 = t.Button(self.finestra, bg="yellow",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.stampaCarrello)
        self.etichetta3 = t.Label(self.finestra, text="Stampa carrello")
        self.pulsante3.grid(row=2, column=0)
        self.etichetta3.grid(row=2, column=1, sticky="w")

        self.pulsante4 = t.Button(self.finestra, bg="green",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.svuotaCarrello)
        self.etichetta4 = t.Label(self.finestra, text="Svuota carrello")
        self.pulsante4.grid(row=3, column=0)
        self.etichetta4.grid(row=3, column=1, sticky="w")

        self.pulsante5 = t.Button(self.finestra, bg="blue",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.acquistoSgabelloRandom)
        self.etichetta5 = t.Label(self.finestra, text="Acquisto sgabello random")
        self.pulsante5.grid(row=4, column=0)
        self.etichetta5.grid(row=4, column=1, sticky="w")

        self.pulsante6 = t.Button(self.finestra, bg="indigo",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.acquistoCassettieraRandom)
        self.etichetta6 = t.Label(self.finestra, text="Acquisto cassettiera random")
        self.pulsante6.grid(row=5, column=0)
        self.etichetta6.grid(row=5, column=1, sticky="w")

        self.pulsante8 = t.Button(self.finestra, bg="black",
                                 width=LARGHEZZA_PULSANTE,
                                 command=self.finestra.quit)
        self.etichetta8 = t.Label(self.finestra, text="Uscita")
        self.pulsante8.grid(row=6, column=0)
        self.etichetta8.grid(row=6, column=1, sticky="w")
        
        self.etichettaCassettiere = t.Label(self.finestra, text="Totale cassettiere: -")
        self.etichettaCassettiere.grid(row=11, column=2)

        self.etichettaElettriche = t.Label(self.finestra, text="Totale cassettiere elettriche: -")
        self.etichettaElettriche.grid(row=12, column=2)

        self.etichettaSgabelli = t.Label(self.finestra, text="Totale sgabelli: -")
        self.etichettaSgabelli.grid(row=13, column=2)

        self.etichettaFinale = t.Label(self.finestra, text="Totale finale: -")
        self.etichettaFinale.grid(row=14, column=2)

        

        # LISTA CARRELLO
        self.listaCarrello = t.Listbox(self.finestra, width=50, height=12)
        self.listaCarrello.grid(row=0, column=2, rowspan=10)

        # TOTALE
        self.labelTotale = t.Label(self.finestra, text="Totale: 0 €",
                                  bg="brown", fg="white")
        self.labelTotale.grid(row=10, column=2)

        t.mainloop()


# MAIN
main = gestionaleGUI()