q = [1, 6, 3, 8, 1, 9]

# c = [0, 0, 0, 0, 0, 0, 0]

massimo = max(q)

c = [0] * (massimo + 1)

for i in range(len(q)):
    num = q[i]
    c[num] += 1

# c = [0, 2, 0, 1, 0, 0, 1, 0, 1, 1]

k = 0
for i in range(len(c)):
    for j in range(c[i]):
        q[k] = i
        k += 1

print("Lista:", q)
print("Contatori:", c)
