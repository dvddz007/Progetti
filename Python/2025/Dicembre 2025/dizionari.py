studente1 = {
    "nome" : "Luca",
    "eta" : 20,
    "voti" : [1.75, 2, 1, 4]
}

studente2 = dict(name = "Josè", eta = 17, voti = [6, 5, 7, 3])
print(f"Terzo voto di {studente1['nome']}: {studente1["voti"][2]}")

print(studente1)

studente1["eta"] = 25

for i in range(len(studente1["voti"])):
    studente1["voti"][i] += 1

print(f"Studente1 dopo la modifica: {studente1}")
print(studente2)

for k in studente1:
    print(f"Per la chiave {k} il valore è {studente1[k]}")
