from Memoria import Memoria
from time import sleep
from random import randint, random


def main():
    MEM = Memoria(5, 1000)
    for i in range(20):
        MEM.aggiungi(i)
        x = random() #  float compreso tra 0 e 1
        sleep(x / 4) #  aspetta un tempo casuale per non risultare troppo veloce e crashare
        print(MEM)
    return 0

#  se lo inizializzo direttamente, avvio main().
#  se viene importato come modulo, non si avvia.
if __name__ == "__main__":
    main()

    ##################################
    # NON AGGIUNGE VALORI ALLA LISTA #
    ##################################
