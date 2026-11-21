#include <stdio.h>

int main(void) {
    // "numero" é un oggetto che contiene il valore che gli viene assegnato.
    int numero = 7;

    // un puntatore * é una variabile che puó contenere un indirizzo di memoria.
    // l'operatore & permette di ottenere l'indirizzo di memoria di un oggetto.
    int *p = &numero;
    // p é un puntatore a int, inizializzato con l'indirizzo di numero.

    printf("Valore di 'numero': %d\nValore letto da 'p': %d\n", numero, *p);  // legge il valore di "numero" attraverso il puntatore p;
    *p = 20; // modifica il valore di "numero" attraverso il suo puntatore"
    printf("Valore di 'numero': %d\nValore letto da 'p': %d\n", numero, *p);
    printf("Indirizzo di \"numero\": %p\n", (void *)&numero);
    printf("Indirizzo contenuto in \"p\": %p\n", (void *)p);
    return 0;
}