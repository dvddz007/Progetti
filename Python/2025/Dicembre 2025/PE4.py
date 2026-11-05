'''
    Un numero palindromo è un numero che si legge allo stesso modo da sinistra a destra e da destra a sinistra, per esempio 9009.

    Domanda:
    Trova il più grande numero palindromo che può essere ottenuto moltiplicando due numeri a tre cifre (cioè tra 100 e 999).
'''

def isPalindrome(numero: int) -> bool:
    numero = str(numero)
    #  controllo se il numero é uguale al numero letto al contrario con lo slicinig.
    return numero == numero[::-1] #  [start:exit:pass] dall'inizio alla fine andando al contrario


def getMaxPalindrome(A: int, B: int):
    maxPalidrome = 0
    num1 = num2 = 0
    for i in range(B, A-1, -1):
        for j in range(B, A-1, -1):
            val = i * j
            if isPalindrome(val) and val > maxPalidrome:
                maxPalidrome = val
                num1, num2 = i, j
    return maxPalidrome, num1, num2


palindrome, a, b = getMaxPalindrome(100, 999)
print(f"Il palindromo più grande è {palindrome}, ottenuto da {a} * {b}")
