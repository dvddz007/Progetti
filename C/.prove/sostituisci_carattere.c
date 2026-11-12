#include <stdio.h>

int main(void) {
    /*
        Dichiara char testo[] = "programmare";.
        Chiedi il carattere da cercare e quello con cui sostituirlo, usando " %c".
        Controlla entrambe le letture: se una fallisce, stampa un errore e termina.
        Scorri la stringa fino a '\0', senza usare strlen.
        Sostituisci ogni occorrenza del carattere cercato e conta le sostituzioni.
        Stampa la stringa risultante e il conteggio.
    */
    char testo[] = "programmare";
    char daRimuovere;
    char sostituto;
    int esito;
    printf("Inserire un carattere da rimuovere nella stringa:\n");
    esito = scanf(" %c", &daRimuovere);
    if (esito != 1) {
        printf("Il valore inserito non é valido\n");
        return 1;
    }
    printf("Inserire un carattere con cui sostituire '%c' nella stringa:\n", daRimuovere);
    esito = scanf(" %c", &sostituto);
    if (esito != 1) {
        printf("Il valore inserito non é valido\n");
        return 1;
    }
    printf("Caratteri da rimuovere: %c\nCaratteri con cui rimpiazzare: %c\n", daRimuovere, sostituto);
    size_t i = 0;
    size_t occorrenze = 0;
    while (testo[i] != '\0') {
        if (testo[i] == daRimuovere) {
            occorrenze++;
            testo[i] = sostituto;
        }
        i++;
    }
    printf("Testo formattato: %s\n", testo);
    printf("Sostituzioni effettuate: %zu", occorrenze);
    return 0;
}