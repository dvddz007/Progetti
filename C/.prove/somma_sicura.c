#include <stdio.h>
#include <limits.h>

bool controllaEsito(int num) {
    if (num == 1) {
        return true;
    }
    return false;
} 

int main(void) {
    /*
        Leggi due int, controllando entrambe le assegnazioni.
        Per ora accetta soltanto valori non negativi, già rappresentabili come int.
        Prima di sommarli, verifica se il risultato supererebbe INT_MAX.
        Stampa la somma oppure "Somma non rappresentabile".
    */
    int a;
    int b;
    printf("Inserire A:\n");
    int esito = scanf("%d", &a);
    if (!controllaEsito(esito) || a < 0) {
        printf("Lettura di A non valida.\n");
        return 1;
    }
    printf("Inserire B:\n");
    esito = scanf("%d", &b);
    // il secondo operando della OR viene controllato solo se il primo é falso.
    if (!controllaEsito(esito) || b < 0) {
        printf("Lettura di B non valida.\n");
        return 1;
    }
    // per non calcolare a + b che potrebbe risultare in overflow
    // a + b > INT_MAX   diventa   a > INT_MAX - b
    if (a > INT_MAX - b) {
        printf("Somma non rappresentabile\n");
    } else {
        printf("Somma: %d\n", a+b);
    }
    return 0;
}