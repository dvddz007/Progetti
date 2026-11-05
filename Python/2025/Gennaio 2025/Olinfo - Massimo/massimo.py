with open("massimo.input0.txt", "r") as fi, open("massimo.output0.txt") as fo:
    n = next(fi)
    n = int(n)
    s = next(fi)
    q = s.split()

    massimo = q[0]
    for i in range(1, n):
        if q[i] > massimo:
            massimo = q[i]

        fo.write("Il valore massimo è: " + str(massimo))
