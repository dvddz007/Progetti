from random import randint, choice
from time import sleep


def main():
    p1 = []
    p2 = []
    mazzo = (crea_mazzo())
    print(crea_briscola(mazzo))
    pesca(p1, p2, mazzo)
    print(f"Mazzo 1: {p1}\nMazzo 2: {p2}")
    print(mazzo)


def crea_mazzo():
    mazzo = [i for i in range(1, 41)]
    mazzo_figura_seme = []
    for carta in range(len(mazzo)):
        seme = mazzo[carta] // 10
        if mazzo[carta] % 10 == 0:
            seme -= 1
        if seme == 0:
            seme = "BASTONI"
        if seme == 1:
            seme = "COPPE"
        if seme == 2:
            seme = "DENARI"
        if seme == 3:
            seme = "SPADE"

        figura = mazzo[carta] % 10
        if figura == 0:
            figura = 10
        if figura == 10:
            figura = "RE"
        if figura == 9:
            figura = "CAVALLO"
        if figura == 8:
            figura = "FANTE"
        if figura == 1:
            figura = "ASSO"
        mazzo_figura_seme.append(randint(1, 41))
    return mazzo_figura_seme


def pesca(p1, p2, mazzo):
    while len(p1) < 3:
        p1.append(mazzo[0])
        mazzo.remove(mazzo[0])

    while len(p2) < 3:
        p2.append(mazzo[0])
        mazzo.remove(mazzo[0])

    return p1.sort(), p2.sort()


def crea_briscola(mazzo):
    briscole = []
    briscola = choice(mazzo)
    mazzo.remove(briscola)
    mazzo.append(briscola)

    if mazzo[carta] condizione:
      dsjaosddsoja
    elif mazzo[carta] condizione:
      sdaadf

    return briscola


main()
