#include <stdio.h>


int main(void) {
    int quantita;
    float larghezza;	// 32 bit vs double con 64 bit
    float altezza;
    int tipo;
    int consegna;
    float sconto;
    printf(
        "Inserire i seguenti valori:\n"
        " - Quantitá volantini\n"           //  Da 1 a 10 000
        " - Larghezza in centimetri\n"      //  Da 5 a 50, estremi inclusi
        " - Altezza in centimetri\n"          //  Da 5 a 70, estremi inclusi
        " - Tipo di stampa\n"               //  1 = bianco e nero, 2 = colori
        " - Consegna\n\n"                   //  1 = standard, 2 = urgente
    );
    // Per leggere e fare scan di un double, si usa %lf perché é un large float.
    // leggere un double con %f provoca un comportamento indefinito.
    int esito = scanf("%d %f %f %d %d", &quantita, &larghezza, &altezza, &tipo, &consegna);
    printf("%d %.2f %.2f %d %d\n", quantita, larghezza, altezza, tipo, consegna);
    printf("Esito: %d\n", esito);
    if (quantita < 1 || quantita > 10000) {
        printf("Il numero di volantini inseriti non é valido.\n");
        return 1;
    } else if (larghezza <= 5.0 || larghezza >= 50.0) {
        printf("La larghezza inserita non é valida.\n");
        return 1;
    } else if (altezza <= 5.0 || altezza >= 70.0) {
        printf("L'altezza inserita non é valida.\n");
        return 1;
    } else if (tipo != 1 && tipo != 2) {
        printf("Il tipo di stampa inserito non é valido.\n");
        return 1;
    } else if (consegna != 1 && consegna != 2) {
        printf("Il tipo di consegna inserito non é valido.\n");
        return 1;
    }
    
    if (quantita >= 100  && quantita < 500) {
    	sconto = 5;
	} else if (quantita >= 500 && quantita < 1000) {
		sconto = 10;
	} else if (quantita >= 1000 && quantita <= 10000) {
		sconto = 15;
	}
    double costo_unitario;
    double costo_stampa;
    double area = larghezza * altezza;
    if (tipo == 1) {
        costo_unitario = area * 0.0002;
    } else {
        costo_unitario = area * 0.0005;
    }
    // da rivedere la formula.
    costo_stampa = ((costo_unitario * quantita) / 100) * sconto;
    printf("Costo stampa: %.2f EUR", costo_stampa);
    return 0;
}
