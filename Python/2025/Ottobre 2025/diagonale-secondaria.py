n = 0
while n < 2:
    n = int(input("Inserire un numero maggiore o uguale di 2: "))

matrice = []
i = 1
for r in range(n):
    lista = []
    for c in range(n):
        lista.append(i)
        i += 1
    matrice.append(lista)

print(f"Matrice {n}x{n}:\n")

for r in range(n):
    for c in range(n):
        elemento = matrice[r][c]
        if elemento < 10:
            print("  " + str(elemento), end="")
        elif 10 <= elemento < 100:
            print(" " + str(elemento), end="")
    print()
print()

print("Diagonale principale:\n")

spazi = " "
for i in range(n):
    if matrice[i][i] < 10:
        print(spazi + " " + str(matrice[i][i]))
    elif 10 <= matrice[i][i] < 100:
        print(spazi + str(matrice[i][i]))
    spazi += " " * 3
print()

print("Diagonale secondaria:\n")

spazi = " " * ((n * 3) - 2)
r = 0
c = -1
slicing = 0
while r != n:
    if matrice[r][c] < 10:
        print(spazi + " " + str(matrice[r][c]))
    elif 10 <= matrice[r][c] < 100:
        print(spazi + str(matrice[r][c]))
    slicing += 3
    spazi = spazi[slicing:]
    r += 1
    c -= 1
