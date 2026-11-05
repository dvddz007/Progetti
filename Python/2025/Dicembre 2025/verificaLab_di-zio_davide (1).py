from random import randint


def stampaTabellare(matrice: list[list[int]]) -> None:
    """
        Stampa una matrice in forma tabellare.
        Gestisce i numeri fino a 1000 escluso.
    """
    for r in range(len(matrice)):
        for c in range(len(matrice[r])):
            val = matrice[r][c]
            if val < 10:
                print(" "*3 + str(val), end="")
            elif 10 <= val < 100:
                print(" "*2 + str(val), end="")
            else:
                print(" " + str(val), end="")
        print()


def creaMatrice(size: int, minimum: int = 1, maximum: int = 99) -> list[list[int]]:
    """
        Crea una matrice che di default ha come range dei numeri 1 e 99 inclusi.
    """
    return [[randint(minimum, maximum) for _ in range(size)] for _ in range(size)]


def trasponi(matrice: list[list[int]]) -> list[list[int]]:
    """
        Crea una matrice trasposta di quella ricevuta come argomento.
        Traspone da riga a colonna.
    """
    size = len(matrice)
    matriceTrasposta = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            matriceTrasposta[c][r] = matrice[r][c]
    return matriceTrasposta


def main() -> None:
    while True:
        try:
            n = int(input("Inserire la grandezza della matrice quadrata: "))
            if n < 2:
                print("La grandezza deve essere maggiore o uguale a 2!\n")
                continue  # faccio riniziare il ciclo

            print(f'Matrice casuale {n}x{n}:')
            matrice = creaMatrice(n)
            stampaTabellare(matrice)

            print()

            print('Matrice trasposta:')
            matriceTrasposta = trasponi(matrice)
            stampaTabellare(matriceTrasposta)

            print()  # riga di abbellimento
            break  # se il try viene eseguito senza errori, termino il while true
        except ValueError:
            print("Il valore deve essere un numero!\n")


main()
