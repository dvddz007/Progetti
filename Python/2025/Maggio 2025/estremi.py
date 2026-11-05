numeri = [1, 2, 3, 4, 5, 6]
estremi = []

inizio = 0
fine = len(numeri) - 1

while inizio <= fine:
    estremi.append(numeri[inizio])
    inizio += 1
    if inizio <= fine:
        estremi.append(numeri[fine])
        fine -= 1

print(estremi)
