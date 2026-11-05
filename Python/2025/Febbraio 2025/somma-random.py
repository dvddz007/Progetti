'''
caricare una lista A con numeri casuali (tra 6 e 12);
caricare una lisat B con input da tastiera;
azzerare nelle due liste i numeri pari;
calcolare la somma degli elementi di A e B;
4 elementi per ogni lista;
'''

import random

a = []
b = []

for i in range(4):
    x=random.randint(6, 12)
    a.append(x)

for i in range(4):
    n = int(input("Inserire un numero: "))
    b.append(n)

print("lista random: ", a)
print("lista in input: ", b)

for i in range(4):
    if a[i] % 2 == 0:
        a[i] = 0
    if b[i] % 2 == 0:
        b[i] = 0

print("liste senza n. pari: ", a, b)

i = 0
somma = 0
while i < 4:
    somma += a[i] + b[i]
    i += 1

print("somma delle liste A e B:", somma)
