#include <stdio.h>


int main(void) {
    /*
        Crea tabellina.c:
            1. Chiedi un intero tra 1 e 10, usando do...while per validarlo.
            2. Usa un for per stampare la sua tabellina da 1 a 10.
    */
   int numero = 0;
   int esito = 0;
    do {
        printf("Inserire il numero di cui calcolare la tabellina (da 1 a 10):\n");
        esito = scanf("%d", &numero);
        printf("Esito: %d\n", esito);
        if (esito != 1) {
            printf("Lettura non valida.\n");
            return 1;
        }
        if (numero < 1 || numero > 10) {
            printf("Il numero inserito non é valido.\n\n");
        }
    } while (numero < 1 || numero > 10); // condizione di continuazione
    
    printf("\nGenero la tabellina di %d:\n", numero);
    for (int i=1; i<11; i++) {
        // %2d e %3d: larghezza minima di 2 e 3 caratteri,
        // con allineamento a destra e spazi a sinistra se necessari.
        printf("%d x %2d = %3d\n", numero, i, numero*i);
    }
    return 0;
}
