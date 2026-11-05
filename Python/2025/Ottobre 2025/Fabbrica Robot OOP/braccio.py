class Braccio:
    #  metodo costruttore
    #  self è il nome dell'oggetto su cui eseguiamo un metodo
    def __init__(self, peso: int | float, angolo: int | float):
        #  metodo usato per inizializzare gli attributi di un oggetto.
        self.peso = peso  # attributo: peso del braccio
        self.angolo = angolo  # attributo: angolo del braccio

    def __str__(self) -> str:
        #  metodo che restituisce delle stringhe se l'oggetto è una stringa
        return f"Braccio di peso {self.peso} Kg., piegato di {self.angolo}°."
