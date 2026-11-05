#VERSIONE 0.1 del 1/10/2024
def calcola(cm,s):
    
    ms=cm*0.80
    print("La maglietta scontata costa:", ms)
    if ms<=s:
        print("Puoi comprare la maglietta")
    else:
        print("Non puoi comprare la maglietta")

#main
    
cm=float(input("Inserire il costo della maglietta: "))
s=float(input("Inserire i soldi posseduti: "))

calcola(cm,s)
