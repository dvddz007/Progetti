import math

def delta(a,b,c):
    d=b*b-4*a*c
    return d
#main

a=float(input("Inserire la A: "))
b=float(input("Inserire la B: "))
c=float(input("Inserire la C: "))
d=delta(a,b,c)

if d > 0 or d < 0:
    x1=(-b+math.sqrt(d)) / (2*a)
    x1=round(x1,3)
    x2=(-b-math.sqrt(d)) / (2*a)
    x2=round(x2,3)
    print("Le soluzioni sono: ",x1,"e",x2)      
    if d == 0:
        x=(-b+math.sqrt(d)) / (2*a)
        round(x,3)
        print("La soluzione è: ",x)
else:
    print("La parabola non ha soluzioni")

print("Il delta equivale a: ",d)
