parole = ["gatto", "cane", "gatto", "uccello", "cane", "topo"]

def occorrenze(parole: list[str]):
    for parola in parole:
        if parole.count(parola) > 1:
            while parola in parole:
                parole.remove(parola)
    return parole


print(occorrenze(parole))
