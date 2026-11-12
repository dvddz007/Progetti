#include <stdio.h>
#include <locale.h> // header che permette al formattazione in un formato locale.


int fattoriale(int n);

int main(void) {
    // controllo dell'installazione del locale.
    if (setlocale(LC_NUMERIC, "it_IT.UTF-8") == NULL) {
        printf("Locale italiano non disponibile.\n"
            "Installare il locale italiano con il seguente comando:\n"
            "sudo locale-gen it_IT.UTF-8\n");
        return 1;
    }

    // LC_NUMERIC       modifica le convenzioni numeriche (virgola, punto per le migliaia...)
    // "it_IT.UTF-8"    richiede il locale indicato con la codifica annessa. deve essere installato nel sistema.
    setlocale(LC_NUMERIC, "it_IT.UTF-8");
    int esito;
    int numero;

    printf("Inserire un numero fra 0 e 12:\n");
    esito = scanf("%d", &numero);
    if (esito != 1 || numero < 0 || numero > 12) {
        printf("Il numero inserito non é valido.\n");
        return 1;
    }
    // %'d é un'estensione POSIX della printf.
    // raggruppa le cifre secondo il locale numerico corrente.
    printf("Il fattoriale di %d é uguale a: %'d\n", numero, fattoriale(numero));
    return 0;
}

int fattoriale(int n) {
    if (n == 0) {
        return 1;
    }
    return n * fattoriale(n-1);
}