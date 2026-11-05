numeri = [4, 2, 7, 4, 8, 2, 9, 2, 7]
frequenza = []

for num in numeri:
    if num in frequenza:
        continue
    elif numeri.count(num) > 1:
        frequenza.append(num)

print(frequenza)