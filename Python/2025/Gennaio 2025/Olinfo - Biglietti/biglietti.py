def biglietti(n, a, m, b):
    s1 = n * a  # caso in cui si comprano solo biglietti
    nc = n // m  # carnet necessari in s2
    r = n % m  # resto di viaggi necessari in s2

    if r == 0:
        # se non ho bisogno di altri biglietti, compro solo carnet
        s2 = nc * b
        s3 = s2
    else:
        # se ho bisogno di altri biglietti, prendo un altro carnet e aggiungo il rimanente in biglietti
        s2 = (nc + 1) * b
        s3 = nc * b + r * a

    if s1 < s2:
        if s1 < s3:
            return s1
        else:
            return s3
    else:
        if s2 < s3:
            return s2
        else:
            return s3


# main

# con with non serve chiudere i file
with open("input.txt", "r") as fi, open("output.txt", "w") as fo:
    p = next(fi).strip()  # legge la riga E toglie gli spazi
    lst = p.split()  # taglia la riga in una lista
    n = int(lst[0])  # cast in intero per la def
    a = int(lst[1])
    m = int(lst[2])
    b = int(lst[3])
    totale = biglietti(n, m, a, b)
    fo.write(str(totale))  # cast in stringa per la funzione write
