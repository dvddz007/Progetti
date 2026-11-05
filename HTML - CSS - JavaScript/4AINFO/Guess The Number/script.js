const score = document.getElementById('score');
const gameElem = document.getElementById('game-section');
const startBtn = document.getElementById('start');
const triesElem = document.getElementById('tries-box');
const chosenNumber = document.getElementById('chosenNumber');
let hint = document.getElementById('hint');
let triesArray = document.getElementById('tries');
let toGuess;
let tentativi;
let points;

function playAgain() {
    tentativi = 0;
    points = 100;
    toGuess = Math.floor(Math.random() * 100);
    triesArray.innerHTML = '';
    chosenNumber.value = '';
    hint.innerHTML = 'Ho pensato a un numero da 0...100, prova a indovinarlo!';
    console.log('Numero casuale = ' + String(toGuess));
}

function addPoints() {
    if (points < 1) {
        points = 1; // minimo di 1 punto
    }
    score.innerHTML = parseInt(score.innerHTML) + points;
}

function addAttempt() {
    // creo la li.
    const li = document.createElement('li');
    // assegno il valore di tentativi nell'html di li.
    li.innerHTML = chosenNumber.value;
    // inserisco la li alla fine della ol.
    triesArray.appendChild(li);
}
function init(status) {
    if (status) {
        gameElem.style.display = 'flex';
        triesElem.style.display = 'flex';
        startBtn.style.display = 'none';
        tentativi = 0;
        points = 100;
        toGuess = Math.floor(Math.random() * 100);
        console.log('Numero casuale = ' + String(toGuess));
    } else {
        gameElem.style.display = 'none';
        triesElem.style.display = 'none';
        startBtn.style.display = 'flex';
        score.innerHTML = '0';
        triesArray.innerHTML = '';
        chosenNumber.value = '';
        hint.innerHTML = 'Ho pensato a un numero da 0...100, prova a indovinarlo!';
        toGuess = null;
        tentativi = null;
        points = null;
    }
}

/*
* Le return servono per ignorare il tentativo inutile/vincente. */
function handle() {
    let number = parseInt(chosenNumber.value);
    if (isNaN(number) || (number < 0 || number > 100)) {
        hint.innerHTML = 'Il numero inserito non é valido.';
        return;

    } else if (number < toGuess) {
        hint.innerHTML = 'Troppo piccolo!';
        tentativi++;
        points -= 10;

    } else if (number > toGuess) {
        hint.innerHTML = 'Troppo grande!';
        tentativi++;
        points -= 10;

    } else {
        hint.innerHTML = 'Hai indovinato!';
        addPoints();
        setTimeout(playAgain, 1000); // imposta un timeout di 1s dove alla fine chiama playAgain.
        return;
    }
    if (points < 1) {
        points = 1;
    }
    addAttempt()
}