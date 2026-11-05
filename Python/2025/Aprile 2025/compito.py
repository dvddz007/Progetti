from random import randint


def creaListaNoDoppioni(n: int) -> list[int]:
    q = []
    while len(q) < n:
        x = randint(1, 100)
        if x not in q:
            q.append(x)
    return q


def controllaListaNoDoppioni(q: list[int]) -> bool:
    for num in q:
        if q.count(num) > 1:
            return False
    return True


for i in range(1000):
    q = creaListaNoDoppioni(10)
    if not controllaListaNoDoppioni(q):
        print("KO")

print("FINE")
