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


saldo_conto = 1000.0
scelta = -1
magazzino = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print("------------------")
print("Programma Fabbrica")
while True:
    print("------------------")
    print(
          "Digitare [ 1 ] per effettuare un versamento sul conto corrente\n"
          "Digitare [ 2 ] per acquistare dei Brick\n"
          "Digitare [ 3 ] per acquistare dei Motori\n"
          "Digitare [ 4 ] per acquistare dei Sensori\n"
          "Digitare [ 5 ] per acquistare delle Batterie Stilo 1,5V\n"
          "Digitare [ 6 ] per acquistare dei Cavi\n"
          "Digitare [ 7 ] per l'assemblaggio dei robot\n"
          "Digitare [ 8 ] per visualizzare il magazzino\n"
          "Digitare [ 9 ] per visualizzare il conto corrente\n"
          "Digitare [ 0 ] per uscire dal programma"
          )

    scelta = int(input("Scegliere un'operazione: "))

    match scelta:
        case 0:
            break
        
        case 1:
            versamento = -1
            while versamento != 0:
                print("------------------")
                print("Digitare [ 0 ] per terminare")
                print("------------------")
                versamento = float(input("Quanto si desidera versare sul conto?\n"))
                saldo_conto += versamento
                print(f"{versamento}€ sono stati aggiunti al contro corrente")

        case 2:
            quantita_brick = -1
            costo_brick = 100
            while quantita_brick != 0:
                print("------------------")
                print("Digitare [ 0 ] per terminare")
                print("------------------")
                quantita_brick = int(input("Quanti Brick si desiderano acquistare?\n"))
                if quantita_brick == 0:
                    break
                if saldo_conto >= (costo_brick * quantita_brick):
                    saldo_conto -= (costo_brick * quantita_brick)
                    magazzino[0] += quantita_brick
                else:
                    print("Saldo insufficiente")
                    break

        case 3:
            quantita_motori_piccoli = -1
            quantita_motori_grandi = -1
            costo_motori_piccoli = costo_motori_grandi = 50

            print("Digitare [ 0 ] per terminare")
            print(
                  "Digitare [ 1 ] per acquistare Motori Piccoli\n"
                  "Digitare [ 2 ] per acquistare Motori Grandi"
                )
            
            tipo = -1
            while tipo not in [1, 2]:
                tipo = int(input("Scegliere il tipo di motore: "))
                if tipo == 1 or tipo == 2:
                    break
                else:
                    print("L'operazione inserita non è valida. Riprova.")

            match tipo:
                case 1:
                    while quantita_motori_piccoli != 0:
                        print("------------------")
                        print("Digitare [ 0 ] per terminare")
                        print("------------------")
                        quantita_motori_piccoli = int(input("Quanti Motori Piccoli si desiderano acquistare?\n"))
                        if quantita_motori_piccoli == 0:
                            break
                        if saldo_conto >= (costo_motori_piccoli * quantita_motori_piccoli):
                            saldo_conto -= (costo_motori_piccoli * quantita_motori_piccoli)
                            magazzino[1] += quantita_motori_piccoli
                        else:
                            print("Saldo insufficiente")
                            break

                case 2:
                    while quantita_motori_grandi != 0:
                        print("------------------")
                        print("Digitare [ 0 ] per terminare")
                        print("------------------")
                        quantita_motori_grandi = int(input("Quanti Motori Grandi si desiderano acquistare?\n"))
                        if quantita_motori_grandi == 0:
                            break
                        if saldo_conto >= (costo_motori_grandi * quantita_motori_grandi):
                            saldo_conto -= (costo_motori_grandi * quantita_motori_grandi)
                            magazzino[2] += quantita_motori_grandi
                        else:
                            print("Saldo insufficiente")
                            break
                
                case _:
                    print("------------------")
                    print("L'operazione inserita non è valida. Riprova.")

        case 4:
            print("------------------")
            quantita_sensori_infrarossi = -1
            quantita_sensori_ultrasuoni = -1
            quantita_sensori_lucecolore = -1

            costo_sensori_infrarossi = costo_sensori_ultrasuoni = costo_sensori_lucecolore = 25

            print("Digitare [ 0 ] per terminare")
            print(
                  "Digitare [ 1 ] per acquistare Sensori Infrarossi\n"
                  "Digitare [ 2 ] per acquistare Sensori Ultrasuoni\n"
                  "Digitare [ 3 ] per acquistare Sensori Lucecolore"
                )

            while True:
                tipo = int(input("Scegliere il tipo di motore: "))
                if tipo in [1, 2, 3]:
                    break
                else:
                    print("L'operazione inserita non è valida. Riprova.")

            match tipo:
                case 1:
                    while quantita_sensori_infrarossi != 0:
                        print("------------------")
                        print("Digitare [ 0 ] per terminare")
                        print("------------------")
                        quantita_sensori_infrarossi = int(input("Quanti Sensori Infrarossi si desiderano acquistare?\n"))
                        if quantita_sensori_infrarossi == 0:
                            break
                        if saldo_conto >= (costo_sensori_infrarossi * quantita_sensori_infrarossi):
                            saldo_conto -= (costo_sensori_infrarossi * quantita_sensori_infrarossi)
                            magazzino[4] += quantita_sensori_infrarossi
                        else:
                            print("Saldo insufficiente")
                            break

                case 2:
                    while quantita_sensori_ultrasuoni != 0:
                        print("------------------")
                        print("Digitare [ 0 ] per terminare")
                        print("------------------")
                        quantita_sensori_ultrasuoni = int(input("Quanti Sensori Ultrasuoni si desiderano acquistare?\n"))
                        if quantita_sensori_ultrasuoni == 0:
                            break
                        if saldo_conto >= (costo_sensori_ultrasuoni * quantita_sensori_ultrasuoni):
                            saldo_conto -= (costo_sensori_ultrasuoni * quantita_sensori_ultrasuoni)
                            magazzino[5] += quantita_sensori_ultrasuoni
                        else:
                            print("Saldo insufficiente")
                            break

                case 3:
                    while quantita_sensori_lucecolore != 0:
                        print("------------------")
                        print("Digitare [ 0 ] per terminare")
                        print("------------------")
                        quantita_sensori_lucecolore = int(input("Quanti Sensori Lucecolore si desiderano acquistare?\n"))
                        if quantita_sensori_lucecolore == 0:
                            break
                        if saldo_conto >= (costo_sensori_lucecolore * quantita_sensori_lucecolore):
                            saldo_conto -= (costo_sensori_lucecolore * quantita_sensori_lucecolore)
                            magazzino[6] += quantita_sensori_lucecolore
                        else:
                            print("Saldo insufficiente")
                            break
                
                case _:
                    print("------------------")
                    print("L'operazione inserita non è valida. Riprova.")

        case 5:
            quantita_batterie_stilo = -1
            costo_batterie_stilo = 5

            while quantita_batterie_stilo != 0:
                print("------------------")
                print("Digitare [ 0 ] per terminare")
                print("------------------")
                quantita_batterie_stilo = int(input("Quante Batterie Stilo 1,5V si desiderano acquistare?\n"))
                if quantita_batterie_stilo == 0:
                    break
                if saldo_conto >= (costo_batterie_stilo * quantita_batterie_stilo):
                    saldo_conto -= (costo_batterie_stilo * quantita_batterie_stilo)
                    magazzino[7] += quantita_batterie_stilo
                else:
                    print("Saldo insufficiente")
                    break

        case 6:
            quantita_cavi = -1
            costo_cavi = 1

            while quantita_cavi != 0:
                print("------------------")
                print("Digitare [ 0 ] per terminare")
                print("------------------")
                quantita_cavi = int(input("Quante Batterie Stilo 1,5V si desiderano acquistare?\n"))
                if quantita_cavi == 0:
                    break
                if saldo_conto >= (costo_cavi * quantita_cavi):
                    saldo_conto -= (costo_cavi * quantita_cavi)
                    magazzino[8] += quantita_cavi
                else:
                    print("Saldo insufficiente")
                    break

        case 7:
            #  assemblaggio robot

        case 8:
            oggetti_magazzino = [
                "Brick",
                "Motori Piccoli",
                "Motori Grandi",
                "Cavi",
                "Sensori Infrarossi",
                "Sensori Ultrasuoni",
                "Sensori Lucecolore",
                "Batterie Stilo 1,5 V",
                "Cavi"
            ]

            print("------------------")
            for i in range(len(magazzino)):
                print(f"{i}) {oggetti_magazzino[i]}: {magazzino[i]}")

        case 9:
            print("------------------")
            print(f"Il saldo del conto ammonta a: {saldo_conto} €")

        case _:
            print("------------------")
            print("L'operazione inserita non è valida. Riprova.")

print("------------------")
print("FINE PROGRAMMA")
