#include <stdio.h>


int setCell();

// definisce nel preprocessore delle variabili che verranno caricate alla chiamata nel file.
// es: setGrid(GRID_ROWS*GRID_COLS)
#define GRID_COLS 30
#define GRID_ROWS 30
#define ALIVE '1'
#define DEAD '0'


int main(void) {
    // inzializzo l'array grid alla grandezza di ROWS*COLS 
    char grid[GRID_ROWS * GRID_COLS];
    setCell();
    printf("%s\n", grid);
    return 0;
}

/* Imposta uno specifico valore della griglia nello stato indicato. */
/* Restitisce 0 o 1 per indicare lo stato di successo. */
int setCell() {
    return 1;
}