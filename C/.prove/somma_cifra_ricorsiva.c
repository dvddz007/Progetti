#include <stdio.h>


int sommaCifre(int n);

int main(void) {
    /*
        - Leggi un intero tra 0 e 1000000, controllando lettura e intervallo.
        - Scrivi int sommaCifre(int n);, con prototipo prima di main e definizione dopo.
        - Restituisci la somma delle cifre decimali usando la ricorsione.
        - Non usare cicli, stringhe, variabili globali o static.
        Esempi: 0 → 0, 427 → 13, 1002 → 3.
    */
    int numero;
    int esito;
    printf("Inserire un numero intero compreso tra 0 e 1.000.000:\n");
    esito = scanf("%d", &numero);
    if (esito != 1 || numero < 0 || numero > 1000000) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    printf("La somma delle singole cifre di '%d' equivale a: %d\n", numero, sommaCifre(numero));
    return 0;
}

int sommaCifre(int n) {
    if (n == 0) {
        return 0;
    }
    return n%10 + sommaCifre(n/10);
}
