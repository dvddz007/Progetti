sequenza = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5]
sottosequenze = []
c = 1  # parti da 1 perchè il primo numero conta come sequenza crescente

for i in range(len(sequenza) - 1):
    if sequenza[i] < sequenza[i + 1]:
        c += 1
    else:
        sottosequenze.append(c)
        c = 1

sottosequenze.append(c)

print(max(sottosequenze))
