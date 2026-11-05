from random import randint

RIGHE = 5
COLONNE = 3
c = 0
m = []

for r in range(RIGHE):
    lista = []
    c = 0
    while c != COLONNE:
        x = randint(-99, -1)
        if x % 2 == 0:
            lista.append(x)
            c += 1
        else:
            x = (2 * x) + 1
            if x > -100:
                lista.append(x)
                c += 1
            else:
                differenza = x + 100
                lista.append(x - differenza + 1)
                c += 1
    m.append(lista)
print(m)

print()

for r in range(RIGHE):
    for c in range(COLONNE):
        if m[r][c] > -10:
            print(" " + str(m[r][c]), end=" ")
        elif m[r][c] <= -10 and m[r][c] > -100:
            print("" + str(m[r][c]), end=" ")
    print()
