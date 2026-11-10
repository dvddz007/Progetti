#include <stdio.h>
#include <string.h>

int main(void) {
    /*
        Dichiara char parola[] = "ciao";.
        Stampa la stringa, sizeof(parola) e strlen(parola).
        Esegui:
            parola[2] = '\0';
            Ripeti le tre stampe.
            Con un ciclo, stampa indice e codice numerico di tutti gli elementi dell’array, anche quelli dopo il primo terminatore.
    */
    char parola[] = "ciao";
    printf(
        "Parola: %s\t"
        "Grandezza: %zu byte\t"
        "Lunghezza: %zu\n",
        parola, sizeof(parola), strlen(parola)
    );
    // printf con %s e strlen si fermano al primo '\0'.
    // gli elementi successivi al primo null terminator rimangono nell'array e sono accessibili per indice.
    parola[2] = '\0';
    printf(
        "Parola: %s\t"
        "Grandezza: %zu byte\t"
        "Lunghezza: %zu\n",
        parola, sizeof(parola), strlen(parola)
    );
    for (size_t i=0; i<sizeof(parola); i++) {
        printf("Indice: %zu\tLettera: %c\tCodice numerico: %d\n", i, parola[i], parola[i]);
    }
    return 0;
}
