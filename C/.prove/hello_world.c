// include un file nell'header del programma.
// .h sta ad indicare un file header.
// la notazione <file> indica proprio un file che il preprocessore cercherá nei percorsi preconfigurati per gli header.
#include <stdio.h>

/*
    tipo del valore che restituisce una funzione,
    nome della funzione,
    parametri della funzione (in questo caso non ce ne sono, quindi void)
*/

int main(void) {
    // void nei parametri equivale a nessun parametro.
    // la printf é una funzione contenuta nell'header stdio.
    printf("Hello World!\nHello World!"); // print del python che NON va a capo automaticamente.
    return 0;   // indica all'ambiente che il programma si é concluso con successo.
}
