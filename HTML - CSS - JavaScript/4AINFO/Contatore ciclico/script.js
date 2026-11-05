const minElem = document.getElementById("minimo");
const maxElem = document.getElementById("massimo");
const counterElem = document.getElementById("counter");

let min = 0;
let max = 0;
let counter = 0;


function updateStyle() {
    // Rimuovo le classi precedenti per evitare il conflitto.
    counterElem.classList.remove('green', 'red', 'black');

    if (counter > 0) {
        counterElem.classList.add('green');
    } else if (counter < 0) {
        counterElem.classList.add('red');
    } else {
        counterElem.classList.add('black');
    }
}


function handleInput() {
    // Number gestisce la stringa vuota portandola a 0.
    const newMin = Number(minElem.value);
    const newMax = Number(maxElem.value);

    // Se é stato inserito solo uno dei due limiti, vado avanti.
    if (minElem.value === "" || maxElem.value === "") {
        return;
    }

    if (isNaN(newMin) || isNaN(newMax)) {
        counterElem.innerHTML = 'I numeri inseriti devono essere degli interi.';
        return;
    }

    if (newMin > newMax) {
        counterElem.innerHTML = 'Il valore MINIMO non puó superare MASSIMO.';
        return;
    }

    min = newMin;
    max = newMax;

    counter = min;
    counterElem.innerHTML = counter;

    updateStyle();
}


function update(value) {
    counter += value;

    // In base al verso in cui ci si avvicina al limite, reimposto il contatore.
    if (counter > max) {
        counter = min;
    } else if (counter < min) {
        counter = max;
    }

    counterElem.innerHTML = counter;
    updateStyle();

    console.log("Value = " + value);
    console.log("Counter = " + counter);
}


function avg() {
    counter = Math.floor((min + max) / 2);
    counterElem.innerHTML = counter;
    updateStyle();
    
    console.log("Value = " + '/2');
    console.log("Counter = " + counter);
}