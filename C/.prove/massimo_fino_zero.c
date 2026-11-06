#include <stdio.h>
//#include <stdbool.h> superfluo perché C23 contiene i booleani come parte del linguaggio


int main(void) {
    /*
        Crea massimo_fino_zero.c:
            - Leggi interi fino all’inserimento di 0.
            - Stampa il massimo dei numeri inseriti, escludendo lo zero finale.
            - Se viene inserito subito 0, stampa "Nessun numero inserito".
            - Se scanf() fallisce, stampa un errore e termina.
            - Usa un while senza array.
        Esempi:
        Input	        Risultato
        4, 9, 2, 0	    Massimo: 9
        -8, -3, -12, 0	Massimo: -3
        0	            Nessun numero inserito
    */
    int numero = -1;
    int esito;
    int massimo;
    bool primo = true;
    
    while (1) {
        printf("Inserire un numero (0 per terminare):\n");
        esito = scanf("%d", &numero);
        if (esito != 1) {
            printf("Il numero inserito non é valido.\n");
            return 1;
        }
        if (numero == 0) {
            break;
        }
        if (primo) {
            massimo = numero;
            primo = false;
        } else {
            if (numero > massimo) {
                massimo = numero;
            }
        }
    }
    if (primo) {
        printf("Nessun numero inserito");
    } else {
        printf("Massimo: %d\n", massimo);
    }
    return 0;
}
