from random import randint

def crescente(q):
    for i in range(len(q)):
        if q[i] < q[i-1]:
            return False
        return True


q = []

for i in range(randint(1, 10)):
    n = int(input("Inserire un numero: "))
    q.append(n)
    
print(f"I numeri {q} sono in ordine crescente?", crescente(q))
