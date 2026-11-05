q = []
n = int(input("Inserire un primo numero: "))

while n != 0:
    for i in range(len(q)):
        print(q)
        if n <= q[i]:
            q.insert(i, n)
            break
    #   entra nella "else" solo se il ciclo non termina con break
    else:
        q.append(n)
        print(q)
    n = int(input("Inserire un altro numero: "))
    
print(q)
