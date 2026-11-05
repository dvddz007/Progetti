# Verificare se una matrice è simmetrica
# matrice quadrata che ha la proprietà di essere la trasposta di se stessa.

# 1) Def per effettuare il check per verificare se una matrice è simmetrica (Return Boolean).
# 2) Def per creare una matrice quadrata di numeri randomici.
# 3) Def per creare una matrice quadrata simmetrica di numeri randomici.

# Menù che chiede all'utente che tipo di matrice si vuole creare e verifiche
# che la stessa sia simmetrica o meno.

from random import randint


def creaCasuale(size: int) -> list[list[int]]:
    """Restituisce una matrice quadrata casuale."""
    return [[randint(1, 99) for _ in range(size)] for _ in range(size)]


def creaSimmetrica(size: int) -> list[list[int]]:
    """Restituisce una matrice che ha le due metà specchiate."""
    m = [[randint(1, 99) for _ in range(size)] for _ in range(size)]

    for r in range(size):
        for c in range(r, size):
            if c == r:
                m[r][c] = 0
            else:
                x = randint(1, 99)
                m[r][c] = x
                m[c][r] = x
    return m


def isSimmetrica(m: list[list[int]]) -> bool:
    """Restituisce un booleano se le due metà sono specchiate."""
    size = len(m)
    for r in range(size):
        for c in range(r + 1, size):
            if m[r][c] != m[c][r]:
                return False
    return True


def creaPerimetrale(size: int) -> list[list[int]]:
    """Restituisce una matrice piena e cambia i bordi con un valore casuale univoco."""
    bordo = randint(1, 99)
    m = [[randint(1, 99) for _ in range(size)] for _ in range(size)]

    for r in range(size):
        for c in range(size):
            if r in [0, size - 1] or c in [0, size - 1]:
                m[r][c] = bordo
    return m


def isPerimetrale(m: list[list[int]]) -> bool:
    """Ignora i valori interni al perimetro.
    Restituisce un booleano se il perimetro della matrice è uguale."""
    numero = m[0][0]  # numero del perimetro
    for r in range(len(m)):
        for c in range(len(m[r])):
            if (r in [0, len(m) - 1] and m[r][c] != numero) or (c in [0, len(m) - 1] and m[r][c] != numero):
                return False
    return True


def gestisciMatrice(funzione, tipo: str) -> None:
    """Gestisce dei controlli su una funzione.
    Restituisce None in caso di errore."""
    try:
        size = int(input(f"Inserisci la dimensione della matrice {tipo}: "))
        if size <= 0:
            print("Errore: la dimensione deve essere positiva.")
            return
    except ValueError:
        print("Errore: inserisci un numero intero valido.")
        return

    matrice = funzione(size)
    print("\nMatrice generata:")
    stampa(matrice)
    print(
        f"La matrice {'non è' if not isSimmetrica(matrice) else 'è'} simmetrica\n"
        f"La matrice {'non è' if not isPerimetrale(matrice) else 'è'} perimetrale"
    )


def stampa(m: list[list[int]]):
    """Stampa in forma tabellare una matrice."""
    for r in range(len(m)):
        for c in range(len(m[r])):
            numero = m[r][c]
            if numero < 10:
                print(" ", str(numero), end="")
            elif 10 <= numero < 100:
                print("", str(numero), end="")
            else:
                print(str(numero), end="")
        print()


while True:
    try:
        scelta = int(input(
            "\nSelezionare un'azione:\n"
            "[ 1 ] per creare una matrice casuale\n"
            "[ 2 ] per creare matrice simmetrica\n"
            "[ 3 ] per creare matrice perimetrale\n"
            "[ 0 ] per termina il programma.\n"
        ))
    except ValueError:
        print("Errore: inserisci un numero intero valido.")
        continue  # ferma il ciclo e passa all'iterazione successiva

    match scelta:
        case 0:
            print("FINE PROGRAMMA.")
            break
        case 1:
            gestisciMatrice(creaCasuale, "casuale")
        case 2:
            gestisciMatrice(creaSimmetrica, "simmetrica")
        case 3:
            gestisciMatrice(creaPerimetrale, "perimetrale")
        case _:
            print("Scelta non valida.")
