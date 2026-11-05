#include <stdio.h>


int main(void) {
    /*
        Crea tabellina.c:
            1. Chiedi un intero tra 1 e 10, usando do...while per validarlo.
            2. Usa un for per stampare la sua tabellina da 1 a 10.
    */
   int numero;
    do {
        printf("Inserire il numero di cui calcolare la tabellina (da 1 a 10):\n");
        scanf("%d", &numero);
        if (numero < 1 || numero > 10) {
            printf("Il numero inserito non é valido.\n\n");
        }
    } while (numero < 1 || numero > 10);
    printf("\nGenero la tabellina di %d:\n", numero);
    for (int i=1; i<11; i++) {
        // 2d e 3d -> riservano n caratteri a sinistra di un (in questo caso) decimale
        printf("%d x %2d = %3d\n", numero, i, numero*i);
    }
    return 0;
}
