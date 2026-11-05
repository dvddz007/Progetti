#Risolvere un'equazione di primo grado
#VERSIONE 0.2del 25/09/2024

def eqne(m,n):
    return -n/m

#main
m=float(input("Inserire il coefficente di X :"))
n=float(input("Inserire il termine noto: "))

if m==0:
    print("Manca il coefficente della X: impossibile risolvere l'equazione.")
else:
    print("La X vale: ", eqne(m,n))
