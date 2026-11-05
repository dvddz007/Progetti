'''
    Se elenchiamo tutti i numeri naturali minori di 10 che sono multipli di 3 o 5, otteniamo:

    3, 5, 6, 9

    La somma di questi numeri è 23.

    Scrivi un programma in Python che calcoli la somma di tutti i numeri naturali minori di 1000 che sono multipli di 3 oppure di 5.
'''

def multipli3_5(target: int) -> int:
    somma = 0
    for i in range(target):
        if (i % 3 == 0) or (i % 5 == 0):
            somma += i
    return somma


print(multipli3_5(1000))
