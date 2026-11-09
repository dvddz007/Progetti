const inputNumberElem = document.getElementById("inputNumber");
const shownNumberElem = document.getElementById("shownNumber");
const startBtnElem = document.getElementById("start");
let timer;
let intervallo;

function start() {
    if (!inputNumberElem.value || inputNumberElem.value < 0) {
        shownNumberElem.innerHTML = "Il numero inserito non è valido."
        return;
    }
    console.log("Timer started.");
    startBtnElem.disabled = true;
    let i = parseInt(inputNumberElem.value);
    shownNumberElem.innerHTML = i;

    timer = setTimeout( ()=> {
        clearInterval(intervallo);
        shownNumberElem.innerHTML = "BOOM!";
        startBtnElem.disabled = false;
        clearTimeout(timer);
        console.log("Timer finished.")
    }, parseInt(inputNumberElem.value) * 1000);

    intervallo = setInterval( ()=> {
        i--;
        shownNumberElem.innerHTML = i;
    }, 1000)
}


function abort() {
    console.log("Timer aborted.");
    clearTimeout(timer);
    clearInterval(intervallo);
    startBtnElem.disabled = false;
    shownNumberElem.innerHTML = "Terminato dall'utente"
}