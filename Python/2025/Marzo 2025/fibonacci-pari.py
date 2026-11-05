a, b = 1, 1
somma = 0

while True:
    c = a+b
    if c % 2 == 0:
        somma += c
    if c >= 4_000_000:
        break
    a, b = b, c

print(somma)
