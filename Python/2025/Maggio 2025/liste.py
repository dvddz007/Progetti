'''
Esercizio 12: Trova l'indice del massimo

Data una lista di numeri interi, trova l'indice della prima occorrenza del valore massimo, senza usare il metodo index().

numeri = [3, 7, 2, 9, 5, 9]
# Risultato atteso: 3 # (prima volta che compare 9)

numeri = [3, 7, 2, 9, 5, 9]

massimo = numeri[0]
maxindex = 0
for i in range(len(numeri)):
    if massimo < numeri[i]:
        massimo = numeri[i]
        maxindex = i

print(maxindex)
'''

'''
Esercizio 13: Elimina tutti gli zeri consecutivi

Data una lista di numeri interi, rimuovi tutti gli zeri che compaiono consecutivamente (lasciandone solo uno al massimo).

numeri = [1, 0, 0, 2, 0, 0, 0, 3, 0, 4]
# Risultato atteso: [1, 0, 2, 0, 3, 0, 4]
'''

'''
numeri = [1, 0, 0, 2, 0, 0, 0, 3, 0, 4]

i = 0
while i < len(numeri) -1:
    if numeri[i] == 0 and numeri[i+1] == 0:
        numeri.pop(i+1)
    i += 1
print(numeri)
'''

'''
Esercizio 15: Trova l'elemento con la massima differenza dai vicini

Data una lista di numeri, trova l'elemento (non il primo né l'ultimo) che ha la maggiore differenza assoluta con la media dei due vicini.

lista = [3, 8, 10, 4, 9, 2]
# Risultato atteso: 10  # (vicini: 8 e 4, media = 6 → diff = 4)
'''

'''
def avg(n, m: int) -> float:
    return round((n + m) / 2)


lista = [3, 8, 10, 4, 9, 2]

maxdif = 0
massimo = 0

for i in range(1, len(lista)-1):
    media = avg(lista[i-1], lista[i+1])
    diff = abs(lista[i] - media)
    if diff > maxdif:
        maxdif = diff
        massimo = lista[i]

print(massimo)
'''

'''
Esercizio 14: Rimuovi elementi tra duplicati

Data una lista, rimuovi tutti gli elementi che si trovano tra la prima e l'ultima occorrenza di un valore duplicato, compresi i duplicati stessi.

lista = [1, 2, 3, 4, 2, 5, 6]
# Risultato atteso: [1, 5, 6]  # tutto da 2 a 2 incluso viene rimosso
'''

'''
lista = [1, 2, 3, 4, 2, 5, 6]

start = 0
finish = 0

for i in range(len(lista)):
    if lista.count(lista[i]) > 1:
        start = lista[i]
        startind = i
        for j in range(i+1, len(lista)):
            if start == lista[j]:
                finish = lista[j]
                finishind = j
                break
        del lista[startind:finishind+1]  # rimuovo i valori da starting a finishind escluso (+1 per rimuoverlo)
        # la DEL rimuove una porzione di valori dalla lista. a differenza della pop o la remove, non rimuove un solo valore.
        break

print(lista)
'''

'''
Esercizio 3: Inverti gruppi di tre elementi

Scrivi un programma che divida la lista in gruppi di 3 elementi e li inverta (ma non usare slicing annidato).

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

Se la lunghezza non è multiplo di 3, ignora gli elementi finali non completi.
'''

'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(lista)-2, 3):  # exit a -2 perchè l'ultimo elemento è len(list)-2 e il primo indice è 0
    lista[i], lista[i+1], lista[i+2] = lista[i+2], lista[i+1], lista[i]

print(lista)
'''

'''
Esercizio 4: Sposta tutti gli 0 alla fine

Sposta tutti gli zeri alla fine della lista, mantenendo l’ordine degli altri elementi.

lista = [1, 0, 2, 0, 3, 4]
# Output: [1, 2, 3, 4, 0, 0]
'''

'''
lista = [1, 0, 2, 0, 3, 4]

for i in range(len(lista)):
    if lista[i] == 0:
        lista.append(lista[i])
        lista.pop(i)

print(lista)
'''

'''
Esercizio 2 – Sostituisci il massimo tra due zeri

Data una lista, ogni volta che trovi due zeri, sostituisci il numero massimo che c'è tra di loro con uno zero.

lista = [0, 4, 9, 2, 0, 1, 0, 8, 7, 0]

# Risultato atteso: [0, 4, 0, 2, 0, 1, 0, 8, 7, 0]
# (il 9 è stato sostituito da 0)
'''

'''
lista = [0, 4, 9, 2, 0, 1, 0, 8, 7, 0]

for i in range(len(lista)):
    if lista[i] == 0:
        start = i
        for j in range(start+1, len(lista)):
            if lista[j] == 0:
                end = j
                break
        break
massimo = max(lista[start:end+1])  # cerca il massimo nella lista
sublista = lista[start:end+1]  # crea una sottolista tra i due 0
#  la sottolista serve per non controllare tutta la lista e per non avere errori in caso ci sia un numero massimo ripetuto più volte.
k = sublista.index(massimo) + start  # trova l'indice del massimo nella sottolista e somma start per trovare l'indice del massimo nella lista completa
lista[k] = 0

print(lista)
'''

'''
Esercizio 3 – Inversione parziale

In una lista, inverte solo la parte tra due elementi uguali, inclusi quegli elementi.

lista = [1, 5, 3, 9, 2, 5, 6]

# Output atteso: [1, 5, 2, 9, 3, 5, 6]
# → la parte da 5 a 5 è stata invertita
'''

'''
lista = [1, 5, 3, 9, 2, 5, 6]

for i in range(len(lista)):
    if lista.count(lista[i]) > 1:
        start = i
        for j in range(start+1, len(lista)):
            if lista[j] == lista[start]:
                end = j
                break
        break

#  Cambio solo i valori in un preciso intervallo
lista[start:end+1] = lista[start:end+1][::-1]  # il [::-1] inverte una lista.
#  Lo slicing ha [start:exit:pass]. se si omettono valori lo slicing parte dall'inizio.
#  Facendo così lo slicing parte dall'inizio fino alla fine e legge la lista al contrario.

print(lista)
'''
