/**
 * Resetta tutti i campi al valore originale.
 */
function reset() {
    document.getElementById("op1").value = "";
    document.getElementById("op2").value = "";
    document.getElementById("operation").value = "+";
    document.getElementById("result").innerText = "0";
    document.getElementById("op2").hidden = false;
    document.getElementById("op1").placeholder = "Primo operando";
    document.getElementById("op2").placeholder = "Secondo operando";
}

/**
 * Nasconde o mostra il secondo operando in base all’operazione selezionata.
 * Nel caso della radice, mostra entrambi gli input ma aggiorna i placeholder.
 */
function hide() {
    const operation = document.getElementById("operation").value;

    if (operation === "√") {
        document.getElementById("op2").hidden = false;
        document.getElementById("op1").placeholder = "Base della radice";
        document.getElementById("op2").placeholder = "Numero da radicare";
    } else {
        document.getElementById("op2").hidden = false;
        document.getElementById("op1").placeholder = "Primo operando";
        document.getElementById("op2").placeholder = "Secondo operando";
    }
}

/**
 * Esegue calcoli in base alla option della select "operations".
 */
function calculate() {
    // il .value è usato solo nel campo input
    const input1 = parseFloat(document.getElementById("op1").value);      // casting
    const input2 = parseFloat(document.getElementById("op2").value);
    const operation = document.getElementById("operation").value;       // prende l'operazione selezionata
    let result;     // creo la variabile, inizialmente senza un valore

    // se uno degli input (is Not a Number) e non ho scelto i radicali, esco dalla funzione
    if (operation !== "√" && (isNaN(input1) || isNaN(input2))) {
        document.getElementById("result").innerText = "Gli input devono essere numeri.";
        return;
    }

    // match-case
    switch (operation) {
        case "+":
            result = input1 + input2;
            break;

        case "-":
            result = input1 - input2;
            break;

        case "*":
            result = input1 * input2;
            break;

        case "/":
            if (input2 !== 0) {
                result = input1 / input2;
            } else {
                result = "Non è possibile dividere per 0."
            }
            break;

        case "%":
            result = input1 % input2;
            break;

        case "^":
            result = input1 ** input2;
            break

        case "√":
            if (input1 === 0) {
                result = "La base della radice deve essere diversa da 0.";
              // se il numero è negativo e la base è pari
            } else if (input1 % 2 === 0 && input2 < 0) {
                result = "Non è possibile calcolare la radice pari di un numero negativo.";
            } else {
                // numero, base
                result = Math.pow(input2, 1 / input1);
            }
            break;

        // case _:
        default:
            result = "Il campo selezionato non è valido."
    }

    // se è un numero, lo formatto a 2 decimali e tolgo zeri senza valenza
    if (typeof result === "number") {
        result = parseFloat(result.toFixed(2));     // equivalente del :.2f
    }
    document.getElementById("result").innerText = result;
}