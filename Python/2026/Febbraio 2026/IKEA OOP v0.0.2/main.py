from Cassettiera import Cassettiera
from Sgabello import Sgabello


#  il self viene usato solo nelle classi, mai nel main.
ca = Cassettiera(2) #  istanza della classe cassettiera
cb = Cassettiera(3) #  istanza della classe cassettiera
cc = Cassettiera(3) #  istanza della classe cassettiera

ca.aggiungiCassetto(1, "fiore")
cb.aggiungiCassetto(2, "mela")
cc.aggiungiCassetto(3, "penna")

print(f"Cassettiera A: {ca}")
print(f"Cassettiera B: {cb}")
print(f"Cassettiera C: {cc}")

sa = Sgabello(3, 120, 30, 140)
sb = Sgabello(2, 100, 10, 110)

print(f"Sgabello A: {sa}")
print(f"Sgabello B (pre metodo): {sb}")
sb.aggiungiGamba()
print(f"Sgabello B (post metodo): {sb}")
