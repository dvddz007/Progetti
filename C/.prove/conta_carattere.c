#include <stdio.h>

int main(void) {
    /*
        1. Dichiara char testo[] = "programmare";.
        2. Leggi con scanf(" %c", ...) il carattere da cercare e controlla l’esito.
        3. Scorri la stringa fino a '\0', senza strlen.
        4. Conta quante volte compare il carattere e stampa il conteggio.
        Usa size_t per indice e conteggio.
        Esempi: cercando 'r' ottieni 3, cercando 'a' ottieni 2, cercando 'z' ottieni 0.
        Mantieni tutto in main e verifica anche il caso testo[] = "".
    */
    char testo[] = "";
    char carattere;

    printf("Stringa: %s\n", testo);
    printf("Inserire un carattere da cercare: ");
    int esito = scanf("%c", &carattere);
    if (esito != 1) {
        printf("Il carattere inserito non é valido.\n");
        return 1;
    }
    size_t i = 0;
    size_t conteggio = 0; // size_t perché é progettato per rappresentare le dimensioni degli oggetti.
    while (testo[i] != '\0') {
        if (testo[i] == carattere) {
            conteggio++;
        }
        i++;
    }
    printf("Il carattere '%c' é presente %zu volte.\n", carattere, conteggio);
    return 0;
}