def calcola_somma(n):
    s = 0
    d = 1   # primo numero dispari
    while n < 0:
        n = int(input("Il numero inserito deve essere maggiore di 0: "))
    c = n
    while c != 0:
        s += d  # s = s + d
        d += 2
        c -= 1
    return s

n = int(input("Inserire un numero: "))
print(calcola_somma(n))
