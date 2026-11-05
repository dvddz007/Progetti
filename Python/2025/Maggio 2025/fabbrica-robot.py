'''
LA FABBRICA DEI ROBOT

- ha i soldi


- può ricevere versamenti dei finanziatori


- la fabbrica ha pezzi di pura plastica


- può acquistare:
    0) brick                  ( 100 EUR );
    1) motori piccoli         ( 50 EUR );
    2) motori grandi          ( 50 EUR );
    3) cavi                   ( 1 EUR );
    4) sensori infarossi      ( 25 EUR );
    5) sensori ultrasuoni     ( 25 EUR );
    6) sensori lucecolore     ( 25 EUR );
    7) batterie stilo 1,5 V   ( 5 EUR ).


- può costruire:

    1) speed (  1 brick,
                1 sensore infrarossi,
                2 motori grandi,
                3 cavi,
                6 batterie.  )

    2) sumo (   1 brick,
                1 sensore infrarossi
                2 motori grandi,
                2 sensori lucecolore,
                3 cavi,
                6 batterie.  )
'''

from locale import setlocale, LC_ALL, currency

#  imposta tutti gli aspetti locali (data, valuta, numeri...) del programma in italiano
setlocale(LC_ALL, "it_IT")

saldo = 1000.0
magazzino = {
    "Brick": 0,
    "Motori Piccoli": 0,
    "Motori Grandi": 0,
    "Cavi": 0,
    "Sensori Infrarossi": 0,
    "Sensori Ultrasuoni": 0,
    "Sensori Lucecolore": 0,
    "Batterie Stilo 1,5V": 0
}
comandi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "x"]
scelta = -1

while scelta != "x":
    print(
          "------------------\n"
          "Digitare [ 1 ] per effettuare un versamento sul conto corrente\n"
          "Digitare [ 2 ] per visualizzare il conto corrente\n"
          "Digitare [ 3 ] per acquistare dei Motori\n"
          "Digitare [ 4 ] per acquistare dei Brick\n"
          "Digitare [ 5 ] per acquistare dei Sensori\n"
          "Digitare [ 6 ] per acquistare delle Batterie Stilo 1,5V\n"
          "Digitare [ 7 ] per acquistare dei Cavi\n"
          "Digitare [ 8 ] per l'assemblaggio dei robot\n"
          "Digitare [ 9 ] per visualizzare il magazzino\n"
          "Digitare [ x ] per uscire dal programma\n"
          "------------------"
    )
    scelta = input("Digitare un comando: ")

    while scelta not in comandi:
        print(
                f"Il comando inserito non è valido.\n" +
                "I comandi validi sono: " + ", ".join(comandi) +
                "\n------------------"
            )
        scelta = input("Digitare un comando: ")

    if scelta == "1":
        print(f"Saldo corrente: {currency(saldo, international=True)}\n")
        print("Digitare [ x ] per terminare l'operazione.")
        bonifico = input("Inserire l'importo da versare: ")
        while bonifico != "x":
            bonifico_int = int(bonifico)

            if bonifico_int < 0:
                print(f"L'importo da versare non può essere inferiore a {currency(1, international=True)}")
            else:
                saldo += bonifico_int
                print(f"\nHai versato {currency(bonifico_int, international=True)}")

            print("Digitare [ x ] per terminare l'operazione.")
            bonifico = input("Inserire l'importo da versare: ")

    if scelta == "2":
        print(f"Saldo conto corrente: {currency(saldo, international=True)}")

    if scelta == "4":
        costo_brick = 100

        if saldo < costo_brick:
            print("Il saldo disponibile non è sufficiente per l'acquisto." + " ")

        else:
            while saldo >= costo_brick:
                print("Digitare [ x ] per terminare l'operazione.")
                q_brick = input("Inserire la quantità di brick da acquistare: ")

                if q_brick == "x":
                    break

                q_brick = int(q_brick)

                if q_brick < 1:
                    print(
                          "La quantità minima di Brick acquistabili è 1." +
                          "------------------"
                          )
                elif saldo < (q_brick * costo_brick):
                    print(
                          "Il saldo disponibile non è sufficiente per l'acquisto." +
                          "\n------------------"
                          )
                else:
                    magazzino["Brick"] += q_brick
                    saldo -= (q_brick * costo_brick)
                    print(
                          f"Hai acquistato {q_brick} Brick.\n"
                          f"Saldo residuo: {currency(saldo, international=True)}"
                          )
    if scelta == "3":
        pass

    if scelta == "4":
        pass

    if scelta == "5":
        pass

    if scelta == "6":
        pass

    if scelta == "7":
        pass

    if scelta == "8":
        pass

    if scelta == "9":
        pass

print("FINE PROGRAMMA")