def fibonacci(n: int) -> int:
    '''
        Restituisce l'n-esimo numero della serie di Fibonacci.
    '''
    if n < 3:
        return 1

    i = 0
    a = 1
    b = 1
    #   for i in range(1, n-2)
    while i < n-2:
        c = a+b
        a = b
        b = c

        i += 1
    return c

'''n = 1
while n != 0:   
    print(fibonacci(n = int(input("Inserire un numero: "))))'''

for i in range(1, 100):
    print(fibonacci(i))
