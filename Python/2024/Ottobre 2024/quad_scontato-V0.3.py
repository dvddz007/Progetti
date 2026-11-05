#VERSIONE 0.3 del 7/10/2024
'''
dato in input il prezzo di un quaderno,
la percentuale di sconto,
e l'ammontare di soldi che luigi ha in tasca,
scrivere un progreamma che calcola
quanti quaderni riuscirà a comprare spendendo tutti i soldi che ha
'''

def quaderni (cq,s,sl):
    cs=cq*(100-s)/100
    qa=sl//cs
    r=sl-cs*qa
    print("Il resto è: ",r, "EUR") #print di quanti soldi di resto rimangono a luigi
    return int(qa)
    
#main

cq=float(input("Inserire il costo di un quaderno: "))
s=float(input("Inserire lo sconto da applicare: "))
sl=float(input("Inserire i soldi posseduti: "))
ris= quaderni (cq,s,sl)
print ("Puoi comprare" ,ris, "quaderni")