def divisore_while_desc(n):
    n1 = n

    while n1 > 0:
        if n % n1 == 0:
            print(n1)
        n1 -= 1
    
def divisore_while_asc(n):

    n1 = 1

    while n1 != n+1:
        if n % n1 == 0:
            print(n1)
        n1 += 1
        
def primo_while(n):

    if n<4:
        return True
    a=2
    while a<=n//2:
        if n%a==0:
            return False
        a+=1
    return True

def primo_for(n):
        
    

n=int(input("Inserire un numero: "))
divisore_while_desc(n)
print("-")
divisore_while_asc(n)
print("-")
primo_while(n)
print("-")
primo_for(n)