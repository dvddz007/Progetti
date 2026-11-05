#include <stdio.h>


int main(void) {
    /*
        Scrivi un programma che:
        - Chieda base e altezza di un rettangolo, entrambe di tipo double.
        - Le legga con una sola scanf().
        - Controlli che entrambe le assegnazioni siano riuscite.
        - Calcoli e stampi l’area con due cifre decimali solo se la lettura è riuscita.
        - Altrimenti stampi "Input non valido".
    */
    double base;
    double altezza;

    printf("Inserire base e altezza di un rettangolo:\n");
    int esito = scanf("%lf %lf", &base, &altezza);
    if (esito == 2 && (base > 0 && altezza > 0)) {
        printf("Area del rettangolo: %.2f cm2.\n", base * altezza);
    } else {
        printf("Input non valido.\n");
    }
    return 0;
}