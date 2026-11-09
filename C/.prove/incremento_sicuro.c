#include <stdio.h>
#include <limits.h>


int main(void) {
    /*
        - Leggi un int, controllando scanf().
        - Se vale INT_MAX, stampa "Impossibile incrementare" senza eseguire l’addizione.
        - Altrimenti stampa il valore aumentato di uno.
        Per ora supponi che l’eventuale numero digitato sia rappresentabile come int. Prova con 7, 2147483646 e 2147483647.
    */
    int numero;
    printf("Intervallo disponibile: %d %d\n", INT_MIN, INT_MAX);
    printf("Inserire un numero intero:\n");
    int esito = scanf("%d", &numero);
    printf("Esito: %d\n", esito);
    if (esito != 1) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    if (numero == INT_MAX) {
        printf("Impossibile incrementare\n");
    } else {
        numero++;
        printf("%d\n", numero);
    }
    return 0;
}