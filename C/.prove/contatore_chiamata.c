#include <stdio.h>


int contaChiamate(bool azzera);

int main(void) {
    /*
        Dichiara il prototipo int contaChiamate(bool azzera); prima di main.
        Definisci la funzione dopo main, usando un contatore locale static inizializzato a zero.
        Se azzera è true, azzera il contatore e restituisci 0, senza incrementarlo.
        Altrimenti incrementa il contatore e restituisci il nuovo valore.
        In main, esegui cinque chiamate, ciascuna in una printf separata, passando nell’ordine: false, false, true, false, false.
    */
    /*printf("%d %d %d %d %d\n",
        // contaChiamate(false), contaChiamate(false), contaChiamate(true), contaChiamate(false), contaChiamate(false));
        // ritorna: 2 1 0 2 1 (in questa prova)
        // l'ordine di valutazione degli argomenti non é specificato come in altri linguaggi.
        contaChiamate(false), contaChiamate(false), contaChiamate(true), contaChiamate(false), contaChiamate(false));
    */
    printf("Chiamata 1: %d\n", contaChiamate(false));
    printf("Chiamata 2: %d\n", contaChiamate(false));
    printf("Chiamata 3: %d\n", contaChiamate(true));
    printf("Chiamata 4: %d\n", contaChiamate(false));
    printf("Chiamata 5: %d\n", contaChiamate(false));
    return 0;
}

int contaChiamate(bool azzera) {
    static int counter = 0;
    if (azzera) {
        counter = 0;
    } else {
        counter++;
    }
    return counter;
}