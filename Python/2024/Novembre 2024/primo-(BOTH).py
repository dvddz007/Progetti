def primo_for(n):
    if n<4:         # i numeri sotto il 3 sono primi
        return True
# controlliamo i divisori partendo da 2 fino alla metà intera di N + 1 (perchè si python si ferma a n//2-1), incrementando la i di 1 ogni volta
    for i in range(2,n//2+1):
        if n%i==0:          # se n % i ha come resto 0, il numero è divisibile per i e non è primo
            return False
    return True

def primo_while(n):
    if n<4:
        return True
    c=2
    while c<=n//2+1:
        if n%c==0:
            return False
        c+=1
    return True

#main

for n in range(1,20+1):
    print(n,"è",primo_for(n))

print("----------")

a=1
while a<=n:
    print(a,"è",primo_while(a))
    a+=1