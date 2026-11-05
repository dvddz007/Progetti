def pot(b,e):
    n=1
    while e!=0:
        n=n*b
        e=e-1
        print(n)
    return (n)

b=float(input("Inserire la base: "))
e=float(input("Inserire l'esponente: "))

pot(b,e)

