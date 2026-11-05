from random import randint

"""
    Si vuole creare un dizionario "classe" con 7 studenti di cui noti sono nome e media.
"""

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
