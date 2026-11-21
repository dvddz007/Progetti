#include <stdio.h>


void scambia(int *x, int *y);

int main(void) {
    /*
        Dichiara prima di main il prototipo:void scambia(int *x, int *y);
        In main, dichiara int a = 4; e int b = 9;.
        Stampa i valori prima dello scambio.
        Chiama:scambia(&a, &b);

        Definisci la funzione dopo main: usa una variabile temporanea di tipo int per scambiare i valori degli oggetti puntati.
        Stampa in main i valori dopo lo scambio: devono essere a = 9 e b = 4.
    */
    int a = 4;
    int b = 9;
    printf("Valori prima dello scambio:\nA: %d\nB: %d\n", a, b);
    scambia(&a, &b); // inserisco gli indirizzi delle variabili da modificare
    printf("Valori dopo lo scambio:\nA: %d\nB: %d\n", a, b);
    return 0;
}

void scambia(int *x, int *y) {
    // scambio con il valore delle variabili agli indirizzi presi come parametri
    int temp;
    temp = *y; // salvo temporaneamente il valore di ció a cui punta y
    *y = *x; // assegno a ció a cui punta y, ció a cui punta x
    *x = temp; // viceversa
}