'''ogni numero è la somma dei due precedenti
dato un numero N stampare la sequenza di fibacci fino ad N'''

def fibonacci_while(n):
    a=1
    b=1
    i=1
    print(1)
    print(1)
    while i<n-1:
        i+=1
        c=a+b
        print(c)
        a=b
        b=c

def fibonacci_for(n):
    a=1
    b=1
    print(1)
    print(1)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c
        
#main        
        
n=int(input("Inserire la quantità di numeri da stampare: "))
fibonacci_while(n)
print("-----")
fibonacci_for(n)
