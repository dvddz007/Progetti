def desc(n):
    for n in range(n, e, p):
        print(n)
        
def asc(n):
    for n in range(n, e, p):
        print(n)

s=input("Selezionare un countdown: \n 0 per il DECRESCENTE \n 1 per il CRESCENTE \n")
while s != 0 or s != 1:
    
    if s=="0":
        n=int(input("Inserire il numero iniziale: "))
        e=int(input("Inserire il numero finale: "))
        p=int(input("Inserire il numero di descrescita: "))
        
        desc(n)
    elif s=="1":
        n=int(input("Inserire il numero iniziale: "))
        e=int(input("Inserire il numero finale: "))
        p=int(input("Inserire il numero di avanzamento: "))
        
        asc(n)
    else:
        print("Il numero inserito non e' valido. Riprovare")
        s=input("Selezionare un countdown: \n 0 per il DECRESCENTE \n 1 per il CRESCENTE \n")
