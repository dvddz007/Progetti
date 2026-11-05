from math import factorial


def fattoriale_while(n: int) -> int:
    if n == 0:
        return 1

    fattoriale = 1
    counter = n

    while counter >= 1:
        fattoriale *= counter
        counter -= 1

    return fattoriale


def fattoriale_for(n: int) -> int:
    if n == 0:
        return 1

    fattoriale = 1
    for i in range(1, n + 1):
        fattoriale *= i

    return fattoriale


#  controllo delle funzioni
x = int(input("Inserire un numero: "))
print(f"Il fattoriale di {x} è {factorial(x)}" if factorial(x) == fattoriale_for(x) == fattoriale_while(x) else "Una funzione contiene un errore")
