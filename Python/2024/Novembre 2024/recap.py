#la seguente def non restituisce nulla, quindi è una "procedura"
#la seguente def accetta un parametro FORMALE n
def countdown_while(n):
    while n>-1:
        print(n)
        n-=1

#la seguente def non restituisce nulla, quindi è una "procedura"
#la seguente def accetta un parametro FORMALE n
def countdown_for(n):
    for n in range(n, -1, -1):
        print(n)
    
#la seguente def non restituisce nulla, quindi è una "procedura"
#la seguente def accetta un parametro FORMALE n
def divisori_while(n):
    d = 2
    while d <= n:
        if n % d == 0:
            print(d)
        d += 1
    
#la seguente def non restituisce nulla, quindi è una "procedura"
#la seguente def accetta un parametro FORMALE n
def divisori_for(n):
    for d in range(2, 1 + n//2):
        if n % d == 0:
            print(d)
    print(n)
    
def primo_while(n):

    if n<4:
        return True
    a=2
    while a<=n//2:
        if n%a==0:
            return False
        a+=1
    return True


#main
n=0
while n<=1000:
    print (n, primo_while(n))
    n+=1
    
