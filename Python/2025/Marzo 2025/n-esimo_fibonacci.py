esimo = int(input("Inserire l'n-esimo numero primo da trovare: "))

a, b = 1, 1

if esimo == 1:
    print(a)
else:
    for i in range(2, esimo): # inizia da 2 perchè i primi due numeri sono a e b
        c = a + b
        a, b = b, c
    print(b)
