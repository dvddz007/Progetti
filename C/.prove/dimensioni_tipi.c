#include <stdio.h>
#include <limits.h>


int main(void) {
    int numero_piccolo = 7; // 4 byte
    int numero_grande = 10000;

    printf("Bit per byte: %d\n\n", CHAR_BIT); // indica quanti bit contiene un byte nella piattaforma in cui viene compilato il programma
    // nel mio caso 8 bit per byte.

    // sizeof restituisce una dimensione in byte, di tipo size_t.
    // size_t è un tipo intero senza segno usato per rappresentare dimensioni.
    // per stampare un size_t si usa %zu
    printf("Dimensione di int: %zu bit - (%zu byte)\n", sizeof(int) * CHAR_BIT, sizeof(int));
    printf("Dimensione di float: %zu bit - (%zu byte)\n", sizeof(float) * CHAR_BIT, sizeof(float));
    printf("Dimensione di double: %zu bit - (%zu byte)\n", sizeof(double) * CHAR_BIT, sizeof(double));     
    printf("Dimensione di bool: %zu bit - (%zu byte)\n\n", sizeof(bool) * CHAR_BIT,  sizeof(bool));

    printf("Minimo rappresentabile int: %d\n", INT_MIN);
    printf("Massimo rappresentabile int: %d\n\n", INT_MAX);

    printf("Dimensione di numero_piccolo: %zu bit - (%zu byte)\n", sizeof(numero_piccolo) * CHAR_BIT, sizeof(numero_piccolo));
    printf("Dimensione di numero_grande: %zu bit - (%zu byte)\n", sizeof(numero_grande) * CHAR_BIT, sizeof(numero_grande));
}
