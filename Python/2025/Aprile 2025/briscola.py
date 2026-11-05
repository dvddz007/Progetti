# Briscola 0.0.3 del 4 Aprile 2025

# ZONA IMPORT
from random import choice, shuffle

# ZONA DATI GLOBALI
semi    = ["Bastoni", "Coppe", "Denari", "Spade"]
figure  = ["Asso", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Fante", "Cavallo", "Re"]

# ZONA DEF (funzioni/procedure)

# funzione: restituisce un valore
def seme(carta):
    n = carta // 10
    return semi[n]

    
def figura(carta):
    n = carta % 10
    return figure[n]


def crea_mazzo():
    m = []
    for i in range(40):
        m.append(i)
    return m

#########
def crea_briscole(mazzo, briscola):
    briscole = []

    for carta in mazzo:
        if seme(carta) == seme(briscola):
            briscole.append(f"{figura(carta)} di {seme(carta)}")

    for carta in mazzo:
        if carta in briscole:
            mazzo.remove(carta)

    return briscole
############

# procedura: non restituisce nulla (ma fa "qualcosa"!)
def mischia_mazzo(m):
    shuffle(m)


def stampa_carta(c):
    print(figura(c), "di", seme(c))

    
def stampa_mazzo(m):
    for i in range(len(m)):
        print(figura(m[i]), "di", seme(m[i]))
    print("totale:",len(m),"carte")
    print("-------------------------------")


################################################
# main
################################################

print("stampo il mazzo appena comprato")
mazzo = crea_mazzo()
stampa_mazzo(mazzo)
print("stampo il mazzo appena mischiato")
mischia_mazzo(mazzo)
stampa_mazzo(mazzo)

prese_pc=[] # le carte che ha preso il pc
prese_p1=[] # le carte che ha preso il p1

mano_pc=[]  # le carte che ha in mano il pc
mano_p1=[]  # le carte che ha in mano il p1

for i in range(39,36,-1):
    mano_p1.append(mazzo[i])
    mazzo.pop(i)
#    m.remove(m[i]) è la stessa cosa, ma è + complesso, non lo uso
for i in range(36,33,-1):
    mano_pc.append(mazzo[i])
    mazzo.pop(i)

print("La briscola è:")
briscola = mazzo[0]
stampa_carta(briscola)

print("hai in mano:")
stampa_mazzo(mano_p1)
#print("stampo la mano di pc")
#stampa_mazzo(mano_pc)

briscole = crea_briscole(mazzo, briscola)

########
print("mazzo senza briscole")
print(mazzo)
print(len(mazzo))
print("briscole")
print(briscole)
print(len(briscole))

print("Briscole", briscole)
########

tavolo = []
turno = "pc"

while len(mazzo) != 0:
    if turno == "pc":
        # gioca il pc
        carta = choice(mano_pc)
        tavolo.append(carta)
        print("PC ha giocato ",end="")
        stampa_carta(carta)
        # gioco io
        scelta = ""
        while scelta not in ["0", "1", "2"]:
            scelta = input("Scegliere la carta da giocare: (0, 1, 2)\n")
        scelta = int(scelta)
        print("P1 ha giocato ",end="")
        stampa_carta(mano_p1[scelta])
        tavolo.append(mano_p1[scelta])
        mano_p1.pop(scelta)
        stampa_mazzo(tavolo)
        break
    
# capire chi ha preso
# aggiornare la variabile turno
# fase di pesca
print("FINE (PER ORA)")
