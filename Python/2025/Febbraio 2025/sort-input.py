q = []

while True:
    n = int(input("Inserire un numero: "))

    if n == 0:
        break

    # inserisce il numero e ferma il ciclo per prenderne un altro
    for i in range(len(q)):
        if n < q[i]:
            q.insert(i, n)
            break
    else:
        # se il numero è maggiore di q[i]
        q.append(n)

    print(q)

print("Lista finale ordinata:", q)
