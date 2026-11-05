#include <stdio.h>


int main(void) {
    int n;  // dichiarazione di una variabile intera senza inizializzarla.
    // una variabile locale, come n, se non inizializzata, ha valore indeterminato.
    printf("Inserire un numero intero:\n");
    // scanf é una funzione input che si trova in stdio
    /*
        Se la conversione fallisce, ad esempio inserendo "ciao",
        scanf non modifica n, che in questo caso rimane indeterminata.
    */

    // Inserendo 3.5 con %d, viene letto l'intero 3;
    // i caratteri ".5" vengono ignorati.
    //      esito = scanf("%d %d", &a, &b)      >1 ciao     esito = 1 con a modificata e b invariata.
    int esito = scanf("%d", &n); // &n sta a indicare l'indirizzo di memoria della variabile n, cioé dove scanf deve scrivere il valore inserito.
    // inserendo 3.5 con l'etichetta %d, verrebbe presa solo la parte decimale del numero.
    if (esito == 1) {
        printf("Valore inserito: %d\nEsito: %d\n", n, esito);
        printf("Valore inserito raddoppiato: %d\n", n*2);
    } else {
        printf("Il valore inserito non é valido.\n");
    }
    return 0;
}