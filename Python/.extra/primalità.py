from math import isqrt


def isPrimo(n: int) -> bool:
    """
    :param n: numero intero da verificare
    :return: True se il numero è primo, False altrimenti.
    """
    if n <= 1:
        return False

    if n in range(2, 3 + 1):
        return True

    #  La radice quadrata ottimizza tutto rendendolo più veloce.
    #  Piuttosto che controllare ogni singolo numero controlla il numero che, moltiplicato per se stesso, da n.

    #  Ciclo senza funzione isqrt:
    #  for i in range(2, int(n**0.5) + 1)

    #  Ciclo senza radice quadrata:
    #  for i in range(2, (n//2) + 1):

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


print(isPrimo(n=int(input("Inserire un numero: "))))
