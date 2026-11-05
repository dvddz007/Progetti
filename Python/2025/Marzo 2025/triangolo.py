s = str(input("Inserire il simbolo della piramide che si desidera: "))
n = int(input("Di che grandezza (orizzontale) si desidera? "))

for i in range(1, n+1):
    print(" " * (n - i) + s * (2 * i - 1))

'''spazi * 6 - i (che scende progressivamente)
+ "*" * (2 (di base) * i (che scende) - 1 (che porta il 2 a 1 nella prima iterazione)'''
