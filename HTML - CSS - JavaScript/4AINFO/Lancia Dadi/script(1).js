const giocatore1PointsElem = document.getElementById("giocatore1Points");
const giocatore2PointsElem = document.getElementById("giocatore2Points");
const roundsElem = document.getElementById("rounds");
const gameElem = document.getElementById("game");
const buttonsElem = document.getElementById("buttons");
const textElem = document.getElementById("text");

let rounds = 0;

const MIN = 1;
const MAX = 6;

function generateNumber() {
    /*
        Arrotonda un numero per eccesso che va da MIN a MAX.
    */
    return Math.floor(Math.random() * MAX) + MIN;
}

function setFace(player) {
    let n = generateNumber();
    document.getElementById(`imgP${player}`).src = `img/${n}.png`;
    return n;
}

function check(a, b) {
    if (a === b) {
        textElem.innerHTML = 'PAREGGIO';
    } else if (a > b) {
        giocatore1PointsElem.innerHTML = parseInt(giocatore1PointsElem.innerHTML) + 1;
        textElem.innerHTML = 'VINCE P1';
    } else {
        giocatore2PointsElem.innerHTML = parseInt(giocatore2PointsElem.innerHTML) + 1;
        textElem.innerHTML = 'VINCE P2';
    }
}

function startGame() {
    let inputRounds = parseInt(document.getElementById("roundCounter").value);

    if (isNaN(inputRounds) || inputRounds <= 0) {
        alert("Inserisci un numero valido di round");
        return;
    }

    rounds = inputRounds;

    roundsElem.classList.add("hidden");
    gameElem.classList.remove("hidden");
    buttonsElem.classList.remove("hidden");
    textElem.classList.remove("hidden");

    giocatore1PointsElem.innerHTML = 0;
    giocatore2PointsElem.innerHTML = 0;
}

function endGame() {
    let p1Score = giocatore1PointsElem.innerHTML;
    let p2Score = giocatore2PointsElem.innerHTML;

    if (p1Score > p2Score) {
        textElem.innerHTML = `FINE PARTITA - VINCE P1 (${p1Score} - ${p2Score})`;
    } else if (p2Score > p1Score) {
        textElem.innerHTML = `FINE PARTITA - VINCE P2 (${p2Score} - ${p1Score})`;
    } else {
        textElem.innerHTML = `FINE PARTITA - PAREGGIO (${p1Score} - ${p2Score})`;
    }

    gameElem.classList.add("hidden");
    buttonsElem.classList.add("hidden");

    roundsElem.classList.remove("hidden");

    document.getElementById("imgP1").src = "img/blank.png";
    document.getElementById("imgP2").src = "img/blank.png";
}

function start() {
    if (rounds <= 0) {
        return;
    }

    let p1 = setFace(1);
    let p2 = setFace(2);
    check(p1, p2);

    rounds--;

    if (rounds === 0) {
        endGame();
    }
}