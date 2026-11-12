#include <stdio.h>


void visita(int n);

int main(void) {
    visita(3);
    return 0;
}

void visita(int n) {
    /*
    Stack chiamate con n=3:
    // ogni chiamata rappresenta un frame.
    // i frame terminano in ordine LIFO (Last-In First-Out).
    
    (gdb) backtrace
    #0  visita (n=0) at C/.prove/ricorsione_traccia.c:12
    #1  0x000055555555519d in visita (n=1) at C/.prove/ricorsione_traccia.c:16
    #2  0x000055555555519d in visita (n=2) at C/.prove/ricorsione_traccia.c:16
    #3  0x000055555555519d in visita (n=3) at C/.prove/ricorsione_traccia.c:16
    #4  0x000055555555515b in main () at C/.prove/ricorsione_traccia.c:7
    */

    // caso base per uscire dalla funzione.
    if (n == 0) {
        return;
    }
    printf("Entro: %d\n", n);
    visita(n - 1); // al ritorno, il codice riprende dall'isitruzione successiva.
    printf("Esco: %d\n", n);
}
