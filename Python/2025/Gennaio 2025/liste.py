def somma(q):
    sum = 0
    for i in range(len(q)):
        sum += q[i]
    return sum


q = [6, 9, 7, 8, 4, 3]

trovato = True

print("somma totale:",somma(q))

print("media secca:", somma(q) / len(q))

print("media arrotondata:", round(somma(q) / len(q), 2))

print("divisione intera:", somma(q) // len(q))


i=0
n = len(q)

while i < n:
    if q[i] == 3:
        print(trovato)
    i += 1

# è uguale a dire "if trovato == True"
if trovato:
    print("ho trovato un 3")
else:
    print("non ho trovato un 3")