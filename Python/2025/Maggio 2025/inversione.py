from random import randint

print("----------------------")
print("LISTA INVERTITA MANUALMENTE:\n")  # MODIFICA LA LISTA ORIGINALE MA MOLTO LENTO

lista = [randint(1, 10) for i in range(10)]
print(f"Lista originale: {lista}")

i = 0
j = len(lista)-1

while i < j:
    lista[i], lista[j] = lista[j], lista[i]
    i += 1
    j -= 1

print(f"Lista invertita: {lista}")

print("----------------------\n")

print("LISTA INVERTITA CON IL METODO REVERSE:\n")  # CREA UNA NUOVA LISTA IN MEMORIA ED è VELOCE IN ESECUZIONE

lista = [randint(1, 10) for i in range(10)]
print(f"Lista originale: {lista}")

lista.reverse()

print(f"Lista invertita: {lista}")

print("----------------------\n")

print("LISTA INVERTITA CON LO SLICING:\n")  # MODIFICA LA LISTA ORIGINALE ED è MOLTO VELOCE. Non è assegnabile.

lista = [randint(1, 10) for i in range(10)]
print(f"Lista originale: {lista}")

lista = lista[::-1]

print(f"Lista invertita: {lista}")
print("----------------------")
