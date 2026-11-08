#include <stdio.h>
#include <limits.h>
// #include <stdint.h> // racchiude altri tipi di interi avanzati.

int main(void) {
    // specifiche solitamente generiche per macchina, non sono garantite.
    char c = 1; // intero con segno da 8 bit, 1 byte. rappresentabili valori da -128 a +127
    short s = 2000; // intero con segno da 16 bit, 2 byte. -32768 a +32767
    int i = 5; // intero con segno da 32 bit, 4 byte. -2147483648 a 2147483647
    long l = 10; // intero con segno da 64 o 32 bit, 8 o 4 byte (stessa lunghezza della WORD del microprocessore).
    // usato per registrare indirizzi di memoria.

    
    printf("Bit per byte: %d\n\n", CHAR_BIT); // indica quanti bit contiene un byte nella piattaforma in cui viene compilato il programma
    // nel mio caso 8 bit per byte.

    // sizeof restituisce un unsigned long, che va rappresentato con %lu.
    printf("Dimensione di char: %lu bit - (%lu byte)\n", sizeof(char) * CHAR_BIT, sizeof(char));
    printf("Dimensione di short: %lu bit - (%lu byte)\n", sizeof(short) * CHAR_BIT, sizeof(short));
    printf("Dimensione di long: %lu bit - (%lu byte)\n", sizeof(long) * CHAR_BIT, sizeof(long));
    printf("Dimensione di int: %lu bit - (%lu byte)\n", sizeof(int) * CHAR_BIT, sizeof(int));
    printf("Dimensione di float: %lu bit - (%lu byte)\n", sizeof(float) * CHAR_BIT, sizeof(float));
    printf("Dimensione di double: %lu bit - (%lu byte)\n", sizeof(double) * CHAR_BIT, sizeof(double));     
    printf("Dimensione di bool: %lu bit - (%lu byte)\n\n", sizeof(bool) * CHAR_BIT,  sizeof(bool));

    // INT_MIN: numero intero minimo rappresentabile dalla piattaforma in cui viene compilato il programma.
    // INT_MAX: numero intero minimo rappresentabile dalla piattaforma in cui viene compilato il programma.
    printf("Minimo rappresentabile int: %d\nMassimo rappresentabile int: %d\n\n",
        INT_MIN, INT_MAX);
}
