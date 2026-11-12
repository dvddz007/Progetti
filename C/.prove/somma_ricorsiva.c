#include <stdio.h>


int sommaFino(int n);

int main(void) {
    /*
        Dichiara il prototipo int sommaFino(int n); prima di main.
        Leggi un intero tra 0 e 100, controllando lettura e intervallo.
        Definisci la funzione dopo main.
        La funzione deve restituire la somma degli interi da 1 a n, usando la ricorsione.
        Per n == 0, deve restituire 0.
        Stampa il risultato in main.
    */
    int numero;
    int esito;
    printf("Inserire un numero tra 0 e 100:\n");
    esito = scanf("%d", &numero);
    if (esito != 1 || numero < 0 || numero > 100) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    printf("Sommatoria dei numeri da 0 a %d: %d\n", numero, sommaFino(numero));
    return 0;
}

int sommaFino(int n) {
    // pesante sulla memoria perché aggiunge allo stack 11 frame (incluso lo 0).

    // caso base
    if (n == 0) {
        return 0;
    } else {
        return n + sommaFino(n-1);
    }
}
