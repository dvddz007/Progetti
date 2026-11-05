#versione 0.3

def figura(carta):
    figura=carta%10
    if figura==0:
       figura=10
    return figura

def seme(carta):
    seme=carta//10
    if figura==10:
        seme=0
    if figura==20:
        seme=1
    if figura==30:
        seme=2
    if figura==40:
        seme=3
    return seme

#main

carta=int(input("inserisci una carta: "))
print("la carta è un",figura(carta),"di",seme(carta))