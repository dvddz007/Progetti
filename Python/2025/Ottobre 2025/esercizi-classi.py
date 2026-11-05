"""
Crea una classe chiamata Auto con:

attributo di classe ruote = 4

attributi d'istanza: marca, modello, anno

un metodo descrivi() che restituisce una frase come
"Questa è una Fiat Panda del 2015 con 4 ruote"

👉 Poi prova a creare due oggetti diversi e a cambiare:

l’attributo d'istanza anno di uno

l’attributo di classe ruote per tutti
"""


class Auto:
    ruote = 4

    def __init__(self, marca: str, modello: str | int, anno: int):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi(self):
        return f"Questa è una {self.marca} {self.modello} del {self.anno} con {self.ruote} ruote"


"""
Crea una classe AutoSportiva che eredita da Auto e:

aggiunge un attributo velocita_massima

aggiunge un metodo gara() che restituisce
"La {marca} {modello} può raggiungere {velocita_massima} km/h!"

ridefinisci (override) il metodo descrivi() per aggiungere questa informazione alla descrizione.

Vuoi che ti controlli il codice dopo che lo scrivi?
"""


class AutoSportiva(Auto):

    def __init__(self, marca: str, modello: str | int, anno: int, velocita_massima: int):
        super().__init__(marca, modello, anno)  # carico il metodo init della sua superclasse (genitore)
        self.velocita_massima = velocita_massima

    def gara(self):
        return f"La {self.marca} {self.modello} può raggiungere {self.velocita_massima} km/h!"

    def descrivi(self):
        base = super().descrivi()
        return f"{base}. Inoltre, {self.gara()}"


"""
Crea una classe chiamata ContoBancario con:

attributo privato __saldo

costruttore che lo inizializza

metodi:

get_saldo() → restituisce il saldo

deposita(importo) → aggiunge al saldo (solo se positivo)

preleva(importo) → toglie dal saldo (solo se c’è abbastanza denaro)

__str__() → restituisce una stringa come "Saldo attuale: 1500 €"
"""


class ContoBancario:

    def __init__(self, saldo: int | float):
        self.__saldo = saldo  # attributo privato

    def get_saldo(self):
        return f"{self.__saldo: .2f} EUR"  # : .2f fa il round a 2 cifre decimali

    def deposita(self, importo: int | float):
        if importo > 0:
            self.__saldo += importo
        else:
            print("Errore. L'importo deve essere maggiore di 0.")

    def preleva(self, importo: int | float):
        if importo <= self.__saldo:
            self.__saldo -= importo
        else:
            print("Errore. Il saldo non è sufficiente.")

    def __str__(self):
        return f"Saldo attuale: {self.__saldo: .2f} EUR"


Auto.ruote = 15
macchina1 = Auto("Fiat", "Panda", 1991)
macchina1.anno = 1983
macchina2 = Auto("Alfa", "Romeo", 2005)

print(macchina1.descrivi())
print(macchina2.descrivi())

macchina3 = AutoSportiva("Pejout", 208, 2005, 180)

print(macchina3.descrivi())

conto = ContoBancario(1500)
print(conto.get_saldo())
conto.preleva(250.12)
print(conto.get_saldo())
conto.deposita(13.12)
print(conto.get_saldo())
print(conto)
