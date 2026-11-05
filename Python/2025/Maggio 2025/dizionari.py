persona = {
    # "Value": "Key",
    "Nome": "Luca",
    "Classe": "3A",
    "Voti": [3, 4, 5]
}

persona["Voti"].append(2)

if "Media" not in persona:
    persona["Media"] = sum(persona["Voti"]) / len(persona["Voti"])

print(f'{persona["Nome"]}: \n Voti {persona["Voti"]} \n Media: {persona["Media"]}')

# -----------------------------------------------------

prezzi = {
    "Pane": 1.5,
    "Latte": 1.2,
    "Uova": 2.0
}

print(f'Prezzo latte: {prezzi["Latte"]}')

prezzi["Foo"] = 60

for key in prezzi:
    print(f'{key}: {prezzi[key]}')

print(f'Totale: {sum(prezzi.values())}')  # values è un metodo che restituisce tutti i valori di un dizionario

print("-----------------------------------------------------")

# -----------------------------------------------------

studenti = {
    "Anna": [7, 8, 9],
    "Marco": [6, 5, 7],
    "Luca": [9, 8]
}

print(sum(studenti["Anna"]) / len(studenti["Anna"]))
print(sum(studenti["Marco"]) / len(studenti["Marco"]))
print(sum(studenti["Luca"]) / len(studenti["Luca"]))

print("-----------------------------------------------------")

# -----------------------------------------------------

utenti = {
    "Luca": "ciao123",
    "Marta": "password",
    "Admin": "root42"
}

print(" \n".join([utente for utente in utenti]))

utente = -1

while utente not in utenti:
    utente = input("Inserire il nome dell'utente che vuole accedere: \n").capitalize()

password = input("Inserire la password per l'utente selezionato: \n")

if password != utenti[utente]:
    print("La password inserita non è valida. Riprova.")
else:
    print("Accesso eseguito con successo.")

print("-----------------------------------------------------")

# -----------------------------------------------------
