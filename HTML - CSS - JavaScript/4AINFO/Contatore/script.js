const minElem = document.getElementById("minimo");
const maxElem = document.getElementById("massimo");
const counterElem = document.getElementById("counter");

function setStart() {
    counterElem.innerHTML = String(minElem.value);
}

function update(value) {
    const min = minElem.value;
    const max = maxElem.value;
    let counter = min;
    console.log("Value = " + value);
    console.log("Counter = " + counter);
    if (min > max) {
        counterElem.innerHTML = "I numeri inseriti non sono validi.";
    }

    if (counter < max+1) {
        counter += value;
    } else {
        counter = min;
    }
    counterElem.innerHTML = counter;
    console.log("Value = " + value);
    console.log("Counter = " + counter);
}

function reset() {
    counterElem.innerHTML = Math.floor((min + max) / 2);
}
