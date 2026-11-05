def stati(t):
    if t<0:
        return "Ghiacciata"
    elif t==0:
        return "Equilibrio"
    elif t>0 and t<100:
        return "Liquida"
    else:
        return "Ebollizione"
        
#main

t=float(input("Inserire una temperatura in gradi Celsius: "))
s=stati(t)
print(s)