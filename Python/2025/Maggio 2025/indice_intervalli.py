numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
intervalli = []

for i in range(0, len(numeri), 3):
    try:
        intervalli.append(numeri[i])
    except IndexError:
        break

print(intervalli)
