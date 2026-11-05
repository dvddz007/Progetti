#include <stdio.h>

int main(void) {
    int a = 17;
    int b = 5;
    //  a / b -> restituisce un intero troncando via la parte decimale del quoziente verso 0.
    //  Per salvare la parte decimale della divisione va convertito uno dei due operandi a double PRIMA della divisione stessa.
    //  Nella printf vanno passati i "segnaposti" indicanti il tipo della variabile o espressione che andrá inserita.
    //  %d  ->  decimal (int del python)
    //  %f  ->  double  (numero con delle cifre dopo il decimale) di default con 7 cifre dopo la virgola
    //      -   si puó indicare la precisione di valori dopo la virgola di un double prima del segnaposto nella printf
    printf("Somma: %d\nDifferenza: %d\nProdotto: %d\nQuoziente: %.2f\nResto: %d\n", a+b, a-b, a*b, (double) a/b, a%b);
    return 0;
}