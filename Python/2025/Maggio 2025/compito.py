from random import randint

q = []
n = -1

while n!=0:
    n = int(input("Inserire un numero: "))
    if n>0:
        q.append(n)
        if n == 23:
            q.append(randint(20, 30))

print(f"Lista con numero casuale se c'è il 23: {q}")

i = 0
while i < len(q):
    if q[i] % 7 == 0:
        q.remove(q[i])
    else:
        i += 1

print(f"Lista senza multipli di 7: {q}")

i = 0
while i < len(q)-1:
    if q[i] + q[i+1] == 50:
        q.pop(i)
        q.pop(i)
    else:
        i += 1

print(f"Lista senza i numeri adiacenti che sommati fanno 50: {q}")

if len(q) >= 2:
    q.pop(2)

print(f"Lista senza il penultimo numero: {q}")

if len(q) >= 2:
    q.pop(1)

print(f"Lista senza il secondo numero: {q}")

print(f"Somma della lista: {sum(q)}")
    