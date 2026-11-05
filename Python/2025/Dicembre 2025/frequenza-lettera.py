stringa = "1234567890"

dizionario = {}

for lettera in stringa:
    if lettera not in dizionario:
        dizionario[lettera] = 1
    else:
        dizionario[lettera] += 1

valori = []
for item in dizionario.items():
    valori.append(item[1])

target = max(valori)

for value in dizionario.items():
    #  stampa più casi se hanno la stessa occorrenza.
    if target == value[1]:
        print(f'La lettera {value[0]} è quella con più occorrenze, ne ha {value[1]}')
        break
