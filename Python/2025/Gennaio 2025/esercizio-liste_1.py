'''
caricare una lista di 7 elementi random positivi minori di 100.

1) Stampare il valore più grande;
2) Verificare se presente il numero 35.
'''

from random import randint


l = []

for i in range(7):
    x = randint(0,100)
    l.append(x)
print("Lista casuale:",l)


massimo = l[0]

for i in range(len(l)):
    if massimo < l[i]:
        massimo = l[i]
print("Il valore più grande della lista è:",massimo)


for i in range(len(l)):
    if l[i] == 35:
        print("Il numero 35 è presente nella posizione:",l.index(35))
        break