#include <stdio.h>

int main(void) {
    int quantita;
    double larghezza;
    double altezza;
    int tipo;
    int consegna;

    double costo_unitario;
    double costo_prima_sconto;
    double importo_sconto;
    double costo_stampa;
    double costo_consegna = 0;
    int sconto = 0;

    printf(
        "Inserire i seguenti valori:\n"
        " - Quantita volantini: da 1 a 10000\n"
        " - Larghezza in centimetri: da 5 a 50, estremi inclusi\n"
        " - Altezza in centimetri: da 5 a 70, estremi inclusi\n"
        " - Tipo di stampa: 1 = bianco e nero, 2 = colori\n"
        " - Consegna: 1 = standard, 2 = urgente\n\n"
    );

    // %lf legge un double; & indica l'indirizzo della variabile.
    int esito = scanf(
        "%d %lf %lf %d %d",
        &quantita, &larghezza, &altezza, &tipo, &consegna
    );

    if (esito != 5) {
        printf("Uno dei valori inseriti non e' valido.\n");
        return 1;
    }

    if (quantita < 1 || quantita > 10000) {
        printf("Il numero di volantini inseriti non e' valido.\n");
        return 1;
    } else if (larghezza < 5.0 || larghezza > 50.0) {
        printf("La larghezza inserita non e' valida.\n");
        return 1;
    } else if (altezza < 5.0 || altezza > 70.0) {
        printf("L'altezza inserita non e' valida.\n");
        return 1;
    } else if (tipo != 1 && tipo != 2) {
        printf("Il tipo di stampa inserito non e' valido.\n");
        return 1;
    } else if (consegna != 1 && consegna != 2) {
        printf("Il tipo di consegna inserito non e' valido.\n");
        return 1;
    }

    if (quantita >= 100 && quantita < 500) {
        sconto = 5;
    } else if (quantita >= 500 && quantita < 1000) {
        sconto = 10;
    } else if (quantita >= 1000 && quantita <= 10000) {
        sconto = 15;
    }

    double area = larghezza * altezza;

    if (tipo == 1) {
        costo_unitario = area * 0.0002;
    } else {
        costo_unitario = area * 0.0005;
    }

    costo_prima_sconto = costo_unitario * quantita;
    importo_sconto = costo_prima_sconto * sconto / 100;
    costo_stampa = costo_prima_sconto - importo_sconto;

    if (consegna == 1) {
        if (costo_stampa < 50) {
            costo_consegna = 5;
        }
    } else {
        costo_consegna = 12;
    }

    double imponibile = costo_stampa + costo_consegna;
    double iva = imponibile * 22 / 100;
    double totale = imponibile + iva;

    printf(
        "Quantita volantini: %d\n"
        "Larghezza: %.2lf cm\n"
        "Altezza: %.2lf cm\n"
        "Area di un volantino: %.2lf cm2\n\n",
        quantita, larghezza, altezza, area
    );

    if (tipo == 1) {
        printf("Tipo di stampa: bianco e nero\n\n");
    } else {
        printf("Tipo di stampa: colori\n\n");
    }

    if (consegna == 1) {
        printf("Consegna: standard\n\n");
    } else {
        printf("Consegna: urgente\n\n");
    }

    printf(
        "Costo unitario: %.4lf EUR\n"
        "Costo prima dello sconto: %.2lf EUR\n"
        "Sconto applicato: %d%%\n"
        "Importo dello sconto: %.2lf EUR\n"
        "Costo stampa scontata: %.2lf EUR\n"
        "Costo consegna: %.2lf EUR\n"
        "Imponibile: %.2lf EUR\n"
        "IVA (22%%): %.2lf EUR\n"
        "Costo totale: %.2lf EUR\n",
        costo_unitario,
        costo_prima_sconto,
        sconto,
        importo_sconto,
        costo_stampa,
        costo_consegna,
        imponibile,
        iva,
        totale
    );

    if (totale < 50) {
        printf("Ordine economico\n");
    } else if (totale < 150) {
        printf("Ordine intermedio\n");
    } else {
        printf("Ordine importante\n");
    }

    return 0;
}