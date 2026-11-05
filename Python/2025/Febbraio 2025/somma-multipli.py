somma = 0
n = 0
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        somma += n
    n += 1
print(somma)

somma = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        somma += i
print(somma)