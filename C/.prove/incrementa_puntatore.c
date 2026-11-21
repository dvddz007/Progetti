#include <stdio.h>
#include <limits.h>

bool incrementaSicuro(int *p);

int main(void) {
    int numero;
    int esito;
    printf("INT_MAX = %d\n", INT_MAX);
    printf("Inserire un numero:\n");
    esito = scanf("%d", &numero);
    if (esito != 1) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    printf("Numero inserito: %d\n", numero);
    if (incrementaSicuro(&numero)) {
        printf("Il numero é stato incrementato: %d\n", numero);
    } else {
        printf("Impossibile incrementare ulteriormente il numero %d.\n", numero);
    }
    return 0;
}

bool incrementaSicuro(int *p) {
    // un puntatore é nulla ( *p = NULL ) quando non punta ad un indirizzo di memoria.
    // leggere un puntatore nullo ha comportamento indefinito.
    // se il puntatore é nullo o punta ad un numero al limite dell'overflow.
    if (p == NULL || *p == INT_MAX) {
        return false;
    }
    *p = *p + 1;
    return true;
}