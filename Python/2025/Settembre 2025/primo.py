def primo(n: int) -> bool:
    '''
        Restituisce un booleano per verificare se un numero è primo,
        cioè divisibile SOLO per se stesso e per 1. 
    '''

    '''if n == 0 or n == 1:
        return False
    if n in [2, 3]:
        return True
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True'''

    if n == 0 or n == 1:
        return False
    if n in [2, 3]:
        return True
    i = 2
    while i < n//2+1:
        if n % i == 0:
            return False
        i += 1
    return True

'''n = int(input("Inserire un numero: "))
while n != 0:
    print(primo(n))
    n = int(input("Inserire un numero: "))'''

for i in range(1000):
    if primo(i):
        print(i, end=" ")
