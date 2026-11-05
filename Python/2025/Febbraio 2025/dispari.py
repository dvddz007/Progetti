'''
Prende in input un numero N.
Il numero N deve essere dispari, se non lo è l'utente deve rieseguire l'input.
Generare una lista di 10 numeri casuali di valore compreso tra -7 e +7, e verificare se N è presente in tale lista.
'''

from random import randint


n = int(input("Inserire un numero: "))
while n % 2 == 0:
    n = int(input("Il numero inserito deve essere dispari: "))


q = []

for i in range(10):
    x = randint(-7, 7)
    q.append(x)
print(q)


'''for i in range(len(q)):
    if q[i] == n:
        print(f"Il numero {n} presente nella lista nell'indice", q.index(n))
print(f"Il numero {n} non è presente nella lista")'''


i = 0

while i < len(q):
    if q[i] == n:
        print(f"Il numero {n} presente nella lista nell'indice", i)
    i += 1