import random


def media(q: list[int | float]) -> float:
    return round(sum(q) / len(q), 1)


studente={}
n = int(input("Quanti studenti ci sono nella classe? "))
i = 0
while i < n:
    nome = input("Inserisci il nome dello studente: ")
    nVoti = int(input("Quanti voti ha lo studente: "))
    voti = []

    print("Inserire [ 0 ] per un voto casuale.\n")
    for j in range(nVoti):
        v = float(input("Inserisci il voto: "))
        if v == 0:
            v = round(random.uniform(2, 10))
            print(f"Voto inserito: {v}")
        else:
            while v not in range(2, 10):
                print(f"Il voto {v} non è valido. Riprova.")
                v = float(input("Inserisci il voto: "))
        voti.append(v)
    print()

    mediaVoti = media(voti)
    studente[nome] = mediaVoti
    i += 1

for nome, m in studente.items():
    print(f"Alunno: {nome} | Media: {m}")
    studenteMaxMedia = None
    maxMedia = 0
    if m > maxMedia:
        maxMedia = m
        studenteMaxMedia = nome

print(f"Studente con la media maggiore: {studenteMaxMedia}, {maxMedia}")
# max delle medie?