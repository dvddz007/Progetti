from cassettiera import Cassettiera


#  il self viene usato solo nelle classi, mai nel main.
a = Cassettiera(2) #  istanza della classe cassettiera
b = Cassettiera(3) #  istanza della classe cassettiera
c = Cassettiera(3) #  istanza della classe cassettiera

a.aggiungiCassetto(1, "fiore")
b.aggiungiCassetto(2, "mela")
c.aggiungiCassetto(3, "penna")

print(f"Cassettiera A:\n {a}")
print(f"Cassettiera B:\n {b}")
print(f"Cassettiera C:\n {c}")
