#include <stdio.h>


int main(void) {
    /*
        Leggi un carattere in una variabile char.
        Controlla che la lettura sia riuscita.
        Stampa il carattere e il suo codice numerico.
        Se è una cifra da '0' a '9', stampa anche il valore numerico corrispondente.
        Altrimenti stampa "Non e' una cifra".
    */
    // il C gestisce i char come numeri interi che possono contenere il codice di un carattere.
    // %c stampa il carattere; %d mostra il valore numerico.
    char carattere;     // 1 byte

    printf("Inserire un carattere:\n");
    // lo spazio prima dell'etichetta serve a saltare eventuali newline, spazi o altre tabulazioni nel buffer.
    // se scanf ricevesse 10, leggerebbe solo 1; 0 e la newline rimarrebbero nel buffer dell'input.
    int esito = scanf(" %c", &carattere);
    if (esito != 1) {
        printf("Il carattere inserito non é valido.\n");
        return 1;
    }
    printf("Carattere inserito: %c\n", carattere);
    printf("Codice numerico: %d\n", carattere);
    if (carattere >= '0' && carattere <= '9') {
        printf("Valore numerico: %d\n", carattere - '0');
    } else {
        printf("Non é una cifra.\n");
    }
    return 0;
}