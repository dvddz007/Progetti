def divisori(n):
    a=n
    while a!=0:
        if n%a==0:
            print(a)
        a=a-1
    
n=int(input("Inserire un numero: "))
divisori(n)