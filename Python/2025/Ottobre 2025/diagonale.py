#  Dato in input un un numero N maggiore o uguale di 2
# (e se così non è, ripetere l'inserimento) creare una matrice quadrata
#  di N righe caricata dei numeri in progressione da 1 in poi.
#  stampare la matrice in forma tabellare
#  e stampare la diagonale principale

n = -1
while n < 2:
    n = int(input("Inserire un numero maggiore o uguale di 2: "))

i = 1
matrice = []
for r in range(n):
    lista = []
    for c in range(n):
        lista.append(i)
        i += 1
    matrice.append(lista)

print("Matrice tabellare:")

for r in range(n):
    for c in range(n):
        numero = matrice[r][c]
        if numero < 10:
            print(" ", numero, end="")
        elif 10 <= numero < 100:
            print("", numero, end="")
        else:
            print(numero, end=" ")
    print()

print("Diagonale principale:")

spazi = " "
for i in range(len(matrice)):
    numero = matrice[i][i]
    if numero < 10:
        print(spazi + " " + str(numero))
    if 10 <= numero < 100:
        print(spazi + str(numero))
    spazi += "   "
