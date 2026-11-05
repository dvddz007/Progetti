#  versione = "v1.0.1 del 21/09/2026"
'''
    https://www.alus.it/pubs/CodiceFiscale/index.php?lang=it
'''

VOCALI = ["A", "E", "I", "O", "U"]
DATE = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
    5 : "E",
    6 : "H",
    7 : "L",
    8 : "M",
    9 : "P",
    10 : "R",
    11 : "S",
    12 : "T"
}
COMUNI = []
CARATTERIPARI = {
    'A': 0, '0': 0,
    'B': 1, '1': 1,
    'C': 2, '2': 2,
    'D': 3, '3': 3,
    'E': 4, '4': 4,
    'F': 5, '5': 5,
    'G': 6, '6': 6,
    'H': 7, '7': 7,
    'I': 8, '8': 8,
    'J': 9, '9': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}
CARATTERIDISPARI = {
    'A': 1, '0': 1,
    'B': 0, '1': 0,
    'C': 5, '2': 5,
    'D': 7, '3': 7,
    'E': 9, '4': 9,
    'F': 13, '5': 13,
    'G': 15, '6': 15,
    'H': 17, '7': 17,
    'I': 19, '8': 19,
    'J': 21, '9': 21,
    'K': 2,
    'L': 4,
    'M': 18,
    'N': 20,
    'O': 11,
    'P': 3,
    'Q': 6,
    'R': 8,
    'S': 12,
    'T': 14,
    'U': 16,
    'V': 10,
    'W': 22,
    'X': 25,
    'Y': 24,
    'Z': 23
}
CARATTERICONTROLLO = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
}
GIORNIMESI = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
try:
    with open("comuni.txt", "r", encoding="utf-8") as f:
        for riga in f.readlines():
            riga = riga.replace("\n", "")
            COMUNI.append(riga.split("\t"))
except FileNotFoundError:
    print("Impossibile trovare il file 'comuni.txt'.")
    exit(1)
    

def calcolaCognome(cognome: str) -> str:
    '''
        Dobbiamo ricavare 3 lettere per il cognome.
        Bisogna prendere la prima, la seconda e la terza consonante.
        Però potrebbe anche succedere che ci siano solo due consonanti oppure una sola; in tal caso dopo aver preso le consonanti si inizia a prendere anche le vocali.
        Se ancora mancano altre lettere per completare la nostra stringa di tre caratteri si aggiunge la lettera X.
        I cognomi composti da più parole vanno considerati come se fossero una sola parola.
    '''
    cognome = cognome.upper()
    cognome = cognome.replace(" ", "")
    cognome = cognome.replace("'", "")
    cognomeCalcolato = ""
    for lettera in cognome:
        if lettera not in VOCALI:
            cognomeCalcolato += lettera
            if len(cognomeCalcolato) == 3:
                return cognomeCalcolato
    for lettera in cognome:
        if lettera in VOCALI:
            cognomeCalcolato += lettera
            if len(cognomeCalcolato) == 3:
                return cognomeCalcolato
    cognomeCalcolato += "X" * (3 - len(cognomeCalcolato))
    return cognomeCalcolato


def calcolaNome(nome: str) -> str:
    '''
        Il procedimento che si utilizza per ricavare le tre lettere del nome, è uguale a quello del cognome
        con l'unica differenza che adesso dobbiamo prendere la prima, la terza e la quarta consonante.
        Nel caso non ci sono quattro consonanti, si prendono le prime tre e se ci sono meno di tre consonanti si effettua lo stesso procedimento del cognome.
    '''


    def contaConsonanti(stringa: str) -> int:
        '''
            Conta le consonanti di una stringa.
        '''
        conteggioConsonanti = 0
        for lettera in stringa:
            if lettera not in VOCALI:
                conteggioConsonanti += 1
        return conteggioConsonanti
    

    nome = nome.upper()
    nome = nome.replace(" ", "")
    nome = nome.replace("'", "")
    nomeCalcolato = ""
    counterConsonanti = 0
    if contaConsonanti(nome) < 4:
        return calcolaCognome(nome)
    for lettera in nome:
        if lettera not in VOCALI:
            counterConsonanti += 1
            if counterConsonanti == 2:
                continue
            nomeCalcolato += lettera
            if len(nomeCalcolato) == 3:
                return nomeCalcolato
    for lettera in nome:
        if lettera in VOCALI:
            nomeCalcolato += lettera
            if len(nomeCalcolato) == 3:
                return nomeCalcolato
    nomeCalcolato += "X" * (3 - len(nomeCalcolato))
    return nomeCalcolato


def calcolaData(data: str, sesso: str) -> str:
    '''
        Anno di nascita
            I due numeri dell'anno di nascita sono semplicemente le sue ultime due cifre.

        Mese di nascita
            Per il mese di nascita non dobbiamo inserire il numero del mese, ma una lettera;
            questo perché i mesi sono 12 e lo spazio a disposizione è ristretto ad un carattere solo.

        Giorno di nascita
            Per definire il giorno di nascita ed il sesso di una persona abbiamo a disposizione 2 cifre.
            Nel caso si tratti di un uomo basta usare queste 2 cifre per indicarne semplicemente il giorno di nascita (con lo zero davanti se il giorno è di una sola cifra),
            mentre se si tratta di una donna dobbiamo inserire il giorno di nascita sommato a 40.
    '''
    
        
    def calcolaAnno(anno: str) -> str:
        '''
            Restituisce le ultime due cifre dell'anno di nascita.
        '''
        return anno[2:]   # parto dall'indice 2, compreso, e vado fino alla fine


    def calcolaMese(mese: str) -> str:
        '''
            Restituisce il valore corrispondente alla chiave inserita (mese).
        '''
        return DATE[int(mese)]


    def calcolaGiorno(giorno: str, sesso: str) -> str:
        ''''
            Restituisce il giorno in cui si é nati.
            Aggiunge 0 se é minore di 10.
            Aggiunge 40 se il sesso é "F".
        '''
        if sesso == "F":
            return str(int(giorno) + 40)
        if len(giorno) != 2:
            giorno = "0" + giorno
        return giorno


    if validaData(data):
        sesso = sesso.upper()
        data = data.split("/")
        giorno = data[0]
        mese = data[1]
        anno = data[2]
        return calcolaAnno(anno) + calcolaMese(mese) + calcolaGiorno(giorno, sesso)
    return ""


def validaStringa(stringa: str) -> bool:
    return not any([char.isdigit() for char in stringa])


def validaData(data: str) -> bool:
    '''
        Verifica:
            - Se la data inserita è inferiore al 1900.
            - Bisestalità dell'anno.
            - La corrispondenza tra mese e giorni totali con quelli inseriti.
    '''


    def isBisestile(anno: int) -> bool:
        '''
            Restituisce un booleano in base alla bisestalità dell'anno.
        '''
        return anno % 400 == 0 or (anno % 4 == 0 and anno % 100 != 0)


    if len(data) != 10 or (data[2] != "/" or data[5] != "/"):
        return False
    
    data = data.split("/")
    for char in data:
        if not char.isdigit():
            return False
        
    gg = int(data[0])
    mm = int(data[1])
    aaaa = int(data[2])

    if gg < 1 or gg > 31 or mm < 1 or mm > 31 or aaaa < 1900 or aaaa > 2026:
        return False
    if mm == 2 and isBisestile(aaaa):
        GIORNIMESI[2] = 29
    if gg <= GIORNIMESI[mm]:
        return True
    return False


def calcolaComune(comune: str) -> str:
    '''
        Il luogo di nascita può essere uno degli 8100 comuni d'Italia oppure un paese straniero.
        Il metodo per calcolare il codice corrispondente, è simile a quello per il mese di nascita,
        perché ad ogni comune italiano o stato estero corrisponde un determinato codice formato da 1 carattere alfabetico e 3 caratteri numerici,
        questi codici vengono redatti dalla Direzione generale del Catasto.
        Il mio programma scaricabile al termine di questa pagina carica i codici degli 8100 comuni d'Italia da un file di testo che potrete scaricare insieme ad esso.
        Nota che per quanto riguarda le nazioni estere,
        esistono i codici anche per nazioni che oggi non esistono più come per esempio la Cecoslovacchia o la Germania dell'est,
        va considerato la stato alla data di nascita della persona.
    '''
    comune = comune.upper()
    for c in COMUNI:
        if c[0] == comune:
            return c[1]
    return ""


def letteraControllo(cf: str) -> str:
    '''
        Convertire in numeri i caratteri di posizione pari.
        Convertire in numeri i caratteri di posizione dispari.
        Addizionare tutti i valori ottenuti e dividerli per 26.
    '''

    somma = 0
    for i in range(len(cf)):
        print(CARATTERIDISPARI[cf[i]])
        if i % 2 == 0:
            somma += CARATTERIDISPARI[cf[i]]
        else:
            somma += CARATTERIPARI[cf[i]]
    print(somma)
    print(somma%26)
    return CARATTERICONTROLLO[somma % 26]


def main() -> None:
    while True:
        nome = input("Inserire il nome: ")
        cognome = input("Inserire il cognome: ")
        if validaStringa(nome) and validaStringa(cognome):
            break
        else:
            print("I dati anagrafici inseriti non sono validi.")
    while True:
        dataDiNascita = input("Inserire la data di nascita [GG/MM/AAAA]: ")
        if validaData(dataDiNascita):
            break
        else:
            print("La data inserita non è valida.\n")
    while True:
        sesso = input("Inserire il proprio sesso [M/F]: ")
        if sesso in ["m", "M", "f", "F"]:
            break
        else:
            print("Il sesso inserito non è valido.\n")
    comune = input("Inserire il comune di nascita: ")

    cf = calcolaCognome(cognome) + calcolaNome(nome) + calcolaData(dataDiNascita, sesso) + calcolaComune(comune)
    print(cf + letteraControllo(cf))


if __name__ == "__main__":
    main()
