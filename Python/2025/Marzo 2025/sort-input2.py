'''
prendi in input N. prendere in input N numeri inserendoli in una lista. determinare se la lista è ordinata in maaniera crescente.
'''

q = []
n = int(input("Quanti numeri si vogliono inserire?\n"))

for i in range(n):
    ni = int(input("Inserire un numero: "))
    q.append(ni)


ordinata = True # si mette all'inizio per non fare assegnamenti ripetuti nel for
for j in range(1, n):
    if q[j] < q[j-1]:
        ordinata = False # solo se non sono ordinati la variabile diventa false
        break

print(f'La lista {q} è ordinata? {ordinata}')
