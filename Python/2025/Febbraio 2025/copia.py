from random import randint


def copia(q):
    c = []
    for i in range(len(q)):
        c.append(q[i])
    return c


q = []
for i in range(randint(1, 30)):
    q.append(i)

print("Lista:",q)
print("Copia della lista:",copia(q))
