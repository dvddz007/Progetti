#include <stdio.h>


// void scambia(int x, int y); // prototipo o dichiarazione di una funzione.
// una volta creato il prototipo, puó essere definita in qualunque parte del codice purché non venga chiamata prima della definizione stessa.
void scambia(int x, int y) {
    int temp = x;
    x = y;
    y = temp;
    printf("X: %d\nY: %d\n\n", x, y);
    // una volta effettuato il return di una funzione (in questo caso alla fine della funzione),
    // tutte le variabili usate da questa vengono distrutte.
}

int main(void) {
    /*
        In main, dichiara int a = 4; e int b = 9;.
        Definisci, prima di main, la funzione void scambia(int x, int y).
        Dentro la funzione, scambia i valori di x e y usando una variabile temporanea e stampali dopo lo scambio.
        In main, chiama scambia(a, b) e poi stampa a e b.
    */
    int a = 4;
    int b = 9;
    scambia(a, b);
    printf("A: %d\nB: %d\n", a, b);
    return 0;
}

// definizione della funzione.
/*void scambia(int x, int y) {
    int temp = x;
    x = y;
    y = temp;
    printf("X: %d\nY: %d\n\n", x, y);
}*/