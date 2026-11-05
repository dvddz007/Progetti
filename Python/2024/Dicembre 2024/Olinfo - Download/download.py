def download(n,f,c):
    n=int(n)
    f=int(f)
    c=int(c)
    
    nf=n//f
    r=n%f
    nc=r//c

    return nf,nc

fi=open("input.txt","r")
fo=open("output.txt","w")
s=next(fi)  # legge la prima riga
n=int(s)    # fa il cast in intero della prima riga (numero dei casi)

for i in range(n):
    vuoto=next(fi)  # salta le righe vuote
    s=next(fi)
    s=s.strip() # rimuove gli spazi tra ogni numero

    lista=s.split() # divide la riga per ogni parametro tra le parentesi (di default lo spazio)
    f,c=download(lista[0], lista[1], lista[2])  # f e c sono i valori restituiti dalla def, in questo caso, una tupla

    fo.write("Case #")  #scrive sul file output nel modo richiesto dal sito
    fo.write(str(i+1))  #casta in str perchè la write richiede stringhe per scriverle
    fo.write(": ")
    fo.write(str(f))
    fo.write(" ")
    fo.write(str(c))
    fo.write("\n")
    
fi.close()
fo.close()
