'''
    Il numero 13195 ha i seguenti fattori primi:
    5, 7, 13, 29


    Domanda:
    Trova il più grande fattore primo del numero: 600851475143
'''

import math

def isPrimo(numero: int) -> bool:
    ''''
        Restituisce un booleano che indica se il numero é primo.
    '''
    if (numero < 2):
        return False

    if numero in (2, 3):
        return True

    if (numero % 2 == 0):
        return False

    #  isqrt restituisce solo la parte intera di una radice quadrata.
    for i in range(3, math.isqrt(numero) + 1):
        if (numero % i == 0):
            return False
    return True


def getMaxPrimeDivisor(K: int) -> int:
    '''
        Restituisce il massimo di una lista di divisori primi del numero target.
    '''
    primeDivisors = []
    for num in range(3, math.isqrt(K) + 1):
        if (isPrimo(num)) and (K % num == 0):
            primeDivisors.append(num)
    return max(primeDivisors)


print(getMaxPrimeDivisor(600851475143))
