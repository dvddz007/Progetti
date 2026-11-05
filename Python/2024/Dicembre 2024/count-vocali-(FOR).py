def isVocale(c):    # c è il PARAMETRO FORMALE
    if c=="a":      # nella condizione booleana (if, while) servono
                    # 2 uguali ==
        return True
    if c=="e":
        return True
    if c=="i":
        return True
    if c=="o":
        return True
    if c=="u":
        return True
    return False    # se non si è verificato nessuno dei 5 casi
                    # precedenti, allora esco qui con False

#main
s = input("inserisci tu la stringa: ")
n = len(s)  #il nome len deriva da length (lunghezza)
            #è sempre un numero intero
print(s)
print("la stringa e' lunga",n,"caratteri")

c=0
for i in range(0,n,1):
    #print("ci sono",c,"vocali") riga commentata, disabilitata
    if isVocale(s[i]):
        #print("ci sono",c,"vocali") riga commentata, disabilitata
        c=c+1

print("ci sono",c,"vocali")
