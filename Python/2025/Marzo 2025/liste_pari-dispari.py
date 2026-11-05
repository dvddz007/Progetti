''' generare e stampare due liste casuali di numeri crescenti:
la prima di numeri pari,
la seconda di numeri dispari.
'''

from random import randint

pari = []
dispari = []

for i in range(10):
    n = randint(0, 100)
    if n % 2 == 0:
        pari.append(n)
    else:
        dispari.append(n)
        
pari.sort(), dispari.sort()
        
print(f"Pari: {pari}")
print(f"Dispari: {dispari}")
