def fattoriale(n):
    f=1
    for i in range(1,n):
        f=f*n
    return f
    
n=int(input("Inserire un numero: "))
print("il fattoriale di", n, "è: ",fattoriale(n))