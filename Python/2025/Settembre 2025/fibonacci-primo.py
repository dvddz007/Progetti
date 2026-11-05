def primo(n):
    '''
        Restituisce un booleano per verificare se un numero è primo,
        cioè divisibile SOLO per se stesso e per 1.
    '''
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


def fibonacci(n):
    '''
        Restituisce l'n-esimo numero della serie di Fibonacci.
    '''
    if n < 3:
        return 1

    i = 0
    a = 1
    b = 1
    while i < n-2:
        c = a+b
        a = b
        b = c

        i += 1
    return c


n = -1
while n <= 0:
    n = int(input("Inserire un numero: "))

i = 1
while fibonacci(i) <= n:
    '''if primo(fibonacci(i)):
        print(f"{fibonacci(i)} è primo.")
    else:
        print(f"{fibonacci(i)} non è primo.")'''
    print(f"Il numero {fibonacci(i)} {'non ' if not primo(fibonacci(i)) else ''}è primo.")
    i += 1
