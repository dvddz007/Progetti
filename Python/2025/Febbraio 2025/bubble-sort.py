'''
Scrivere un programma che prenda in input una serie di numeri (arrestandosi quando riceve 0).
Ogni qualvolta viene inserito un numero questo va inserito in una lista q.
L'inserimento del numero nella lista q deve avvenire in ordine.
'''

q = []
n = int(input("Inserire un numero: "))

i = 0
while True:
    if n == 0:
        break
    q.insert(i, n)
    n = int(input("Inserire un altro numero: "))
    i += 1

for i in range(len(q)):
    for j in range(len(q) - 1):  # -1 per non andare fuori dal range
        if q[j] > q[j + 1]:
            q[j], q[j + 1] = q[j + 1], q[j]  # Tuple swap
            # inverte i 2 valori su una linea per non sovrascrivere i valori da subito.
# se i numeri non sono in ordine crescente vengono invertiti

print(q)
