numeri = [3, 5, 3, 7, 5, 9]
non_duplicati = []
counter = 0

for num in range(len(numeri)):
    if numeri[num] not in non_duplicati:
        non_duplicati.append(numeri[num])
    else:
        numeri[num] = "DUPLICATO"

print(numeri)
