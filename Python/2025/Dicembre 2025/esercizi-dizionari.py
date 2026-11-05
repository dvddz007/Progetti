from random import randint


persona = {
    'nome' : 'Luca',
    'cognome' : 'Rossi',
    'eta' : '19',
    'citta' : 'Roma'
}

print(persona.keys())  # restituisce una lista con le chiavi del dizionario.
print(persona.values())  # restituisce una lista con i valori del dizionario.

# itera su una tupla restituita dal metodo items(). 
for key, value in persona.items():
    print(key, value)

print(persona.get('nome'))  # permette di accedere ad un valore del dizionario. 
print(persona.get('NOME'))  # restituisce None se la chiave non esiste.
persona.pop('citta')  # rimuove una chiave e il valore associato. Ne restituisce l'oggetto originario.
print(persona)
persona.clear()  # svuota il dizionario
print(persona)

del persona  # rimuove vari tipi di oggetto



"""
    Si vuole creare un dizionario "classe" con 7 studenti di cui noti sono nome e media.
"""

'''
classe = [
    {"nome" : "Marco", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Andrea", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Piotr", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Davide", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Manuel", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Longoverde", "media" : sum([randint(1, 10) for _ in range(5)]) / 5},
    {"nome" : "Denis", "media" : sum([randint(1, 10) for _ in range(5)]) / 5}
]

for i, studente in enumerate(classe):
    print(f"{i}: {studente['nome']}: {studente}")
'''


'''
    Rimuovi tutti gli elementi usando solo pop()
'''

numeri = {"uno": 1, "due": 2, "tre": 3}
for key in numeri.keys():
    del key
# DA FINIRE
# itera sul dizionario arriando a svuotarlo
