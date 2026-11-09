#include <stdio.h>


double calcolaMedia(int a, int b);

int main(void) {
    /*
        Dichiara prima di main il prototipo double calcolaMedia(int a, int b);.
        Definisci la funzione dopo main: deve calcolare e restituire la media, conservando la parte decimale, senza stampare.
        In main, leggi due interi e controlla scanf().
        Chiama la funzione e stampa il risultato con due cifre decimali.
    */
    int a;
    int b;
    int esito;

    printf("Inserire il valore di A:\n");
    esito = scanf("%d", &a);
    if (esito !=1) { 
        printf("Il valore inserito non é valido.\n");
        return 1;
    }
    printf("Inserire il valore di B:\n");
    esito = scanf("%d", &b);
    if (esito != 1) {
        printf("Il valore inserito non é valido.\n");
        return 1;
    }
    printf("Media: %.2lf\n", calcolaMedia(a, b));
    return 0;
}


double calcolaMedia(int a, int b) {
    return ((double) a + b) / 2.0;
}