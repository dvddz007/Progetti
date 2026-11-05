'''def modifica_lista(lista, valore, nuovo_valore):
    c = lista.count(valore)
    lista.append(valore)

    counter = 0
    for i in range(len(lista)):
        if lista[i] == valore:
            counter += 1
        if counter == 2:
            lista[i] = nuovo_valore
            break
    lista.sort()
    return lista, c


lista = [4, 2, 7, 2, 9]
print(modifica_lista(lista, 2, 5))'''

'''def gestisci_playlist(playlist, nuova_canzone, canzone_da_rimuovere):
    playlist.append(nuova_canzone)
    playlist_copia = playlist.copy()
    if canzone_da_rimuovere in playlist:
        playlist.remove(canzone_da_rimuovere)
    return playlist, playlist_copia


playlist = ["Song A", "Song B", "Song C"]
print(gestisci_playlist(playlist, "Song D", "Song B"))'''

'''def gestisci_coda(coda, nuova_persona, persona_prioritaria, servita):
    coda.append(nuova_persona)
    coda.insert(1, persona_prioritaria)
    if servita in coda:
        coda.remove(servita)
    coda_originale = coda.copy()
    coda.reverse()
    return coda_originale, coda

coda = ["Alice", "Bob", "Charlie"]
print(gestisci_coda(coda, "David", "Eve", "Bob"))'''

'''def gestisci_ordini(ordini, nuovo_ordine, ordine_da_rimuovere):
    ordini.append(nuovo_ordine)
    c = ordini.count(nuovo_ordine)
    if ordine_da_rimuovere in ordini:
        ordini.remove(ordine_da_rimuovere)
    ordini.sort()
    return ordini, c


ordini = ["Pizza", "Pasta", "Insalata", "Pizza"]
print(gestisci_ordini(ordini, "Pizza", "Pasta"))'''

'''def gestisci_presenze(registro, nome, azione):
    c = registro.count(nome)
    if azione == "arrivo":
        registro.append(nome)
    if azione == "assenza":
        if nome in registro:
            registro.remove(nome)
    if azione == "correzione":
        counter = 0
        for i in range(len(registro)):
            if registro[i] == nome:
                counter += 1
                if counter == 2:
                    registro[i] = "Errore"
                    break
    registro.sort()
    return registro, c

registro = ["Alice", "Bob", "Charlie", "Alice"]
print(gestisci_presenze(registro, "Alice", "correzione"))'''

'''def gestisci_coda_stampa(coda, documento, azione):
    coda_originale = coda.copy()
    if azione == "aggiungi":
        coda.append(documento)
    if azione == "priorità":
        coda.insert(1, documento)
    if azione == "stampa":
        if coda:  # controlla se coda è una lista con degli elementi al suo interno
            coda.pop(0)
    coda.reverse()
    return coda_originale, coda


coda = ["Doc1", "Doc2", "Doc3"]
print(gestisci_coda_stampa(coda, "DocX", "priorità"))'''

'''def gestisci_ordini(ordini, nuovo_ordine, ordine_da_rimuovere, azione):
    ordini_originali = ordini.copy()
    if azione == "aggiungi":
        ordini.append(nuovo_ordine)
    if azione == "priorità":
        ordini.insert(0, nuovo_ordine)
    if azione == "rimuovi":
        ordini.remove(ordine_da_rimuovere)
    if azione == "correzione":
        counter = 0
        for i in range(len(ordini)):
            if ordini[i] == nuovo_ordine:
                counter += 1
                if counter == 1:
                    ordini[i] = "Errore"
    if azione == "ordinamento":
        ordini.sort()
    if azione == "inversione":
        ordini.reverse()
    return ordini_originali, ordini


ordini = ["Pizza", "Pasta", "Insalata", "Pizza"]
print(gestisci_ordini(ordini, "Pizza", "Pasta", "correzione"))'''

'''def gestisci_studenti(studenti, nome, azione):
    copia = studenti.copy()
    if azione == "arrivo":
        studenti.append(nome)
    if azione == "assenza":
        studenti.remove(nome)
    if azione == "correzione":
        counter = 0
        for i in range(len(studenti)):
            if studenti[i] == nome:
                counter += 1
                if counter == 2:
                    studenti[i] = "Errore"
    if azione == "copia":
        return copia
    if azione == "conta":
        conta = studenti.count(nome)
        return conta
    if azione == "inversione":
        studenti.reverse()
    if azione == "ordinamento":
        studenti.sort()
    return copia, studenti


studenti = ["Alice", "Bob", "Charlie", "Alice"]
print(gestisci_studenti(studenti, "Alice", "correzione"))'''

'''def gestisci_prenotazioni(prenotazioni, nome, azione):
    copia = prenotazioni.copy()
    if azione == "prenota":
        prenotazioni.append(nome)
    if azione == "annulla":
        prenotazioni.remove(nome)
    if azione == "priorità":
        prenotazioni.insert(0, nome)
    if azione == "sposta":
        print([(i, prenotazione) for i, prenotazione in enumerate(prenotazioni)])
        global posizione
        posizione = int(input("In che posizione si vuole inserire il proprio ordine? "))
        prenotazioni.insert(posizione, nome)
    if azione == "copia":
        return copia
    if azione == "inversione":
        prenotazioni.reverse()
    if azione == "ordinamento":
        prenotazioni.sort()
    return f"Lista originale: {copia}\nLista modificata: {prenotazioni}"


prenotazioni = ["Anna", "Luca", "Marco"]
print(gestisci_prenotazioni(prenotazioni, "Paolo", "sposta"))'''
