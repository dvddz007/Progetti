#include <stdio.h>


int main(void) {
    int quantita;

    /*while (quantita < 1 || quantita > 10000) {
        printf("La quantiá inserita non é valida.\n");
        scanf("%d", &quantita);
    }
    printf("La quantitá inserita é corretta.\n");*/

    do {
        printf("Inserire una quantiá tra 1 e 10000\n");
        scanf("%d", &quantita);
        if (quantita < 1 || quantita > 10000) {
            printf("La quantita inserita non e' valida.\n\n");
        }
    } while (quantita < 1 || quantita > 10000);
    printf("Quantita accettata: %d\n", quantita);
}
