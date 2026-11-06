#include <stdio.h>


int main(void) {
    /*
        Scrivi un programma che:
            - Legga interi uno alla volta.
            - Continui finché l’utente non inserisce 0.
            - Alla fine stampi la somma e quanti numeri sono stati inseriti, escludendo lo zero finale.
            - Termini con un messaggio di errore se scanf() non riesce a leggere un intero.
    */
    int conteggio = 0;
    int somma = 0;
    int numero = 0;
    int esito = 0;
    
    printf("Inserire un numero da sommare (inserire 0 per terminare).\n");
    esito = scanf("%d", &numero);
    if (esito != 1) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    while (numero != 0) {
        somma += numero;
        conteggio++;
        printf("Inserire un numero da sommare (inserire 0 per terminare).\n");
        esito = scanf("%d", &numero);
        if (esito != 1) {
            printf("Il numero inserito non é valido.\n");
            return 1;
        }
    }
    printf("Somma totale: %d\n", somma);
    printf("Numeri inseriti: %d\n", conteggio);
    if (conteggio == 0) {
        printf("Nessun numero inserito\n");
    } else {
        double media = (double) somma / conteggio;
        printf("Media: %.2lf\n", media);
    }
    return 0;
}
