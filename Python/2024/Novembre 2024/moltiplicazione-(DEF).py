def prodotto(a,b):

    n=0
    while b>0:
        n=n+a
        b=b-1
        print(n)
    return n

#main

a=int(input("Inserire un numero positivo intero: "))
b=int(input("Inserire un altro numero positivo intero: "))

print("Il prodotto è:",prodotto(a,b))
