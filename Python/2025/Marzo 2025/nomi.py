'''Scrivere cognomi casuali arrestandosi quando esce un cognome per la terza volta'''

from random import randint

cognomi = ["Ercolino", "Giovannoli", "Longoverde", "Norscia", "Osmani"]
frequenze = [0 for item in cognomi]

# while max(c) != 3:
while 3 not in frequenze:
    i = randint(0, len(cognomi)-1)
    frequenze[i] += 1
    print(cognomi, frequenze)
print("\nFine")
    