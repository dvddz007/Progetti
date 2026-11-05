def divisori_asc(n):
    a=1
    while a <= n:
        if n%a==0:
            print(a)
        a=a+1

n = int(input("Inserire un numero: "))
divisori_asc(n)
