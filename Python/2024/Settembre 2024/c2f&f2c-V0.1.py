def c2f(cc):
    return cc*1.8+32 #return va indentato con TAB
    
def f2c(ff):
    return (ff-32)/1.8
    
#main
#celsius=float(input("Inserire la temperatura in Celsius") #il simbolo = sta per "assegnamento"

celsius= input("Inserire una temperatura in gradi Celsius: ")
celsius= float(celsius)

c=c2f(celsius)

print("La temperatura in Celsius vale: " ,c);
#stampa la conversione della variabile celsius con la def c

f=f2c(celsius)

print("La temperatura in Fahreneit vale: " ,f);