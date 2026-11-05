'''dati in input i lati di un rettangolo, calcolare la misura della diagonale'''

import math

def diag(b,h):
    d=math.sqrt(b*b+h*h)
    return d

#main

b=float(input("Inserire lunghezza del rettangolo: "))
h=float(input("Inserire larghezza del rettangolo: "))

d=diag(b,h)
round(d, 2)

print("La diagonale vale: ",d)
