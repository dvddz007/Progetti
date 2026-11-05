def somme(e):
    a=0
    x=0
    while e>=a:
        n=int(input("Inserire un numero: "))
        a=a+n
        x=x+1
    return x

#main

e=int(input("Inserire la E: "))
print("Sono stati inseriti",somme(e),"numeri")
