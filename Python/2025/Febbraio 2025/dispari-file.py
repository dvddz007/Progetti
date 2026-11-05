i = 0

n = int(input("Inserire un numero: "))
while n % 2 == 0:
    n = int(input("Il numero inserito deve essere dispari: "))


with open("input.txt", "r") as fi:
    s = next(fi)
    s = s.split()
    print(s)
    while i < len(s):
        if int(s[i]) == n:
            print(f"Il numero {n} presente nella lista nell'indice", i)
        i += 1
