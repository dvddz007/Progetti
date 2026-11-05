def divisoriDesc(n):
    n1 = n
    while n1 > 0:
        if n % n1 == 0:
            print(n1)
        n1 -= 1

def divisoriAsc(n):
    n1 = 1
    while n1 != n+1:
        if n % n1 == 0:
            print(n1)
        n1 += 1

#main

n=int(input("Inserire un numero: "))
divisoriDesc(n)
print("-")
divisoriAsc(n)