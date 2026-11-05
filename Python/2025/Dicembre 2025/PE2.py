'''
    Ogni nuovo termine della successione di Fibonacci è generato dalla somma dei due termini precedenti.
    Partendo da 1 e 2, i primi termini della successione sono:

    1, 2, 3, 5, 8, 13, 21, 34, ...

    Considerando i termini della successione di Fibonacci il cui valore non supera quattro milioni, trova la somma di tutti i termini pari.
'''

def fibonacci(target: int) -> int:
    somma = 0
    a = 0
    b = 1
    c = a + b
    while c <= target:
        if (c % 2 == 0):
            somma += c
        a = b
        b = c
        c = a + b
    return somma


print(fibonacci(4_000_000))
