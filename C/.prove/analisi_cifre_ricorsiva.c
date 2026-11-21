#include <stdio.h>


int contaCifre(int n);
int contaOccorrenze(int n, int cifra);
int cifraMassima(int n);

int main(void) {
    /*
        Il programma deve leggere:
            - un intero numero tra 0 e 1000000;
            - una cifra cifra tra 0 e 9, letta come int.
            Controlla entrambe le letture e gli intervalli. Poi usa queste tre funzioni ricorsive:
            int contaCifre(int n);
            int contaOccorrenze(int n, int cifra);
            int cifraMassima(int n);

            Devono restituire, rispettivamente:
                1. Il numero di cifre decimali di n.
                2. Quante volte compare la cifra cercata.
                3. La cifra più grande presente nel numero.
    */
    int esito;
    int numero;
    int daCercare;
    printf("Inserire un numero tra 0 e 1.000.000:\n");
    esito = scanf("%d", &numero);
    if (esito != 1 || numero < 0 || numero > 1000000) {
        printf("Il valore inserito non é valido.\n");
        return 1;
    }
    printf("Inserire una cifra da cercare nel numero precedente:\n");
    esito = scanf("%d", &daCercare);
    if (esito != 1 || daCercare < 0 || daCercare > 9) {
        printf("Il valore inserito non é valido.\n");
        return 1;
    }
    printf(
        "Cifre di \"%d\": %d\n"
        "Occorrenze di \"%d\" in \"%d\": %d\n"
        "Cifra massima di \"%d\": %d\n",
        numero, contaCifre(numero),
        daCercare, numero, contaOccorrenze(numero, daCercare),
        numero, cifraMassima(numero)
    );
    return 0;
}

int contaCifre(int n) {
    // n/10 continua a rimuovere l'ultima cifra del numero
    // (la divisione tra due interi ha come risultato un numero senza virgola)
    //
    // continuo a dividere il numero finché non diventa ad una cifra.
    if (n < 10) return 1;
    return 1 + contaCifre(n/10);
}

int contaOccorrenze(int n, int cifra) {
    // controllo se l'ultima cifra del numero é uguale a "cifra"
    // e continuo a rimuovere questa cifra dal numero finché non diventa <10.
    // la if innestata serve per controllare il caso iniziale in cui si inserisce (0, 0)
    if (n < 10) {
        if (n == cifra) {
            return 1;
        }
        return 0;
    }
    if (n%10 == cifra) {
        return 1 + contaOccorrenze(n/10, cifra);
    }
    // lo 0 non contribuisce alla somma, ovviamente.
    return 0 + contaOccorrenze(n/10, cifra);
}

int cifraMassima(int n) {
    // compara l'ultima cifra con quella massima dei precedenti.
    if (n<10) return n;
    // salvo in m per non ripetere la chiamata ricorsiva.
    int m = cifraMassima(n/10);
    if (n%10 > m) return n%10;
    return m;
}