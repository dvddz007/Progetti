#include <stdio.h>


int main(void) {
    /*
        Scrivi un programma che:
        - Dichiari tre variabili int con valori 7, 8 e 10.
        - Calcoli la media, conservando la parte decimale.
        - Stampi la media con due cifre dopo il punto.
    */

    int a = 7;
    int b = 8;
    int c = 10;

    int somma = a + b + c;
    double media = (double) somma / 3;
    // equivale a fare:
    // double media = somma / 3.0;

    printf("Somma: %d\n", somma);
    printf("Media: %.2f\n", media);
    
    return 0;
}
