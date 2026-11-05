#  Dato in input un un numero N maggiore o uguale di 2
# (e se così non è, ripetere l'inserimento) creare una matrice quadrata
#  di N righe caricata dei numeri in progressione da 1 in poi.
#  stampare la matrice in forma tabellare
#  e stampare la diagonale principale

def main(n: int):
    
    matrice = []
    i = 1
    for r in range(n):
        lista = []
        for c in range(n):
            lista.append(i)
            i += 1
        matrice.append(lista)

    print("Matrice tabellare:\n")

    for r in range(n):
        for c in range(n):
            if matrice[r][c] < 10:
                print(" " * 2 + str(matrice[r][c]), end="")
            elif 10 <= matrice[r][c] < 100:
                print(" " + str(matrice[r][c]), end="")
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
    print("\n")


for i in range(2, 10):
    print(f"Matrice {i}x{i}: \n")
    main(i)
