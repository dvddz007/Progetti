#include <stdio.h>

int main(void) {
    /*
        Dichiara char testo[] = "programmare";.
        Calcola la lunghezza usando un ciclo e un contatore size_t, senza strlen.
        Fermati quando incontri '\0', senza contarlo.
        Stampa la lunghezza con %zu.
        Verifica il programma anche sostituendo l’inizializzazione con "", cioè la stringa vuota.
    */
    char testo[] = ""; // una stringa vuota contiene comunque il null terminator
    size_t i = 0;
    while (testo[i] != '\0') {
        i++;
    }
    printf("Lunghezza: %zu\n", i);
    return 0;
}