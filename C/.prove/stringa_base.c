#include <stdio.h>
//#include <string.h> // header che contiene strlen()


int main(void) {
    /*
        Dichiara char parola[] = "ciao";.
        Stampa la stringa con %s.
        Stampa sizeof(parola) con %zu.
        Usa un for per stampare indice e codice numerico di tutti e cinque gli elementi, incluso il terminatore.
        Cambia la prima lettera in 'C' e ristampa la stringa.
    */
    char parola[] = "ciao"; // con la lunghezza di un array vuota, la sua dimensione viene dedotta dall'inizializzazione + il null terminator.
    // la stringa "ciao" include '\0', quindi l'array contiene 5 elementi.

    l_loop:
    printf("%s\n", parola);
    printf("Grandezza di %s: %zu byte\n", parola, sizeof(parola));
    
    // sizeof restituisce la dimensione dell'intero array in byte.
    // dichiaro i come size_t perché sizeof restituisce un size_t e sarebbe preferibile un confronto tra tipi uguali.
    // size_t é un intero senza segno usato per rappresentare dimensioni in byte.
    for (size_t i=0; i<sizeof(parola); i++) {
        printf("Lettera numero %zu\tLettera: %c\tCodice numerico: %d\n",
        i, parola[i], parola[i]);
    }
    if (parola[0] == 'C') {
        goto l_exit;
    }
    parola[0] = 'C';
    goto l_loop;

    l_exit:
    return 0;
}
