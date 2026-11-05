def potenza(b,e):

    n=1
    while e>0:
        n=n*b
        e=e-1
        print(n)
    return n

#main

b=int(input("Inserire la base: "))
e=int(input("Inserire l'esponente : "))

print("Il prodotto è:",potenza(b,e))
