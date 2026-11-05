#include <stdio.h>


int main(void) {
    int quantita;
    printf("Inserire una quantiá tra 1 e 10000\n");
    scanf("%d", &quantita);

    while (quantita < 1 || quantita > 10000) {
        printf("La quantiá inserita non é valida.\n");
        scanf("%d", &quantita);
    }
    printf("La quantitá inserita é corretta.\n");
}
