#include <stdio.h>


int main(void) {
    /*
        Scrivi un programma che:
        - Chieda due numeri interi, letti con una sola scanf().
        - Controlli che siano stati assegnati entrambi.
        - Se la lettura è riuscita, calcoli e stampi la media con due cifre decimali.
        - Altrimenti stampi "Input non valido", senza calcolare la media.
        Per esempio, con 7 10 deve stampare Media: 8.50; con 7 ciao deve segnalare l’input non valido. Usa valori piccoli per queste prove.
    */

    int a; 
    int b;
    printf("Inserire due numeri interi:\n");
    int esito = scanf("%d %d", &a, &b);
    // se vengono passati piú valori di quanti richiesti alla scanf, quelli verranno letti alla prossima scanf.
    if (esito == 2) {
        printf("I numeri sono stati inseriti correttamente.\n");
        double media = ((double) a + b) / 2; 
        printf("Media dei numeri: %.2f\n", media);
    } else {
        printf("Input non valido.\n");
    }
    return 0;
}
