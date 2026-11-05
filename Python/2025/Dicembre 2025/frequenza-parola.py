from os import path


while True:
    try:
        file = input("Inserire il nome di un file da aprire: ")
        with open(f'{file}.txt', 'r') as fi:
            frase = fi.readlines()
            break
    except FileNotFoundError:
        print(f'Il file {file} non esiste!')
        continue

# da copnmtinuare

print(f"{frase=}")

dizionario = {}

for parola in frase:
    if parola not in dizionario:
        dizionario[parola] = 1
    else:
        dizionario[parola] += 1

valori = []
for item in dizionario.items():
    valori.append(item[1])

target = max(valori)

for value in dizionario.items():
    #  stampa più casi se hanno la stessa occorrenza.
    if target == value[1]:
        print(f'La lettera {value[0]} è quella con più occorrenze, ne ha {value[1]}')
        break

