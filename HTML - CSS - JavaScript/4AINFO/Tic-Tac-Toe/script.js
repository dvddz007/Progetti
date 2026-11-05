/*
    Disposizione matrice:

    | box1 | box2 | box3 |
    | box4 | box5 | box6 |
    | box7 | box8 | box9 |
*/

const box1 = document.getElementById('box1');
const box2 = document.getElementById('box2');
const box3 = document.getElementById('box3');
const box4 = document.getElementById('box4');
const box5 = document.getElementById('box5');
const box6 = document.getElementById('box6');
const box7 = document.getElementById('box7');
const box8 = document.getElementById('box8');
const box9 = document.getElementById('box9');
const turnElem = document.getElementById('turn');
let turn; // turno iniziale
let xPoints = document.getElementById('p1Points'); // container punti di X
let oPoints = document.getElementById('p2Points'); // container punti di O
let x = 0; // counter punti di X
let o = 0; // counter punti di O

// l'attributo onload vuole una funzione.
window.onload = function() {
    setTurn();
}

/*
* Restituisce un numero decimale tra 0 e 1, esclusi.*/
function randomFloat() {
    return Math.random();
}

/*
* Genera un numero casuale, lo stampa in console e converte il turno corrente.*/
function setTurn() {
    let rnd = (randomFloat());
    console.log('Numero casuale: ' + rnd);
    /*if (rnd < 0.5) {
     turn = 'X';
    } else {
        turn = 'O';
    }*/
    turn = rnd < 0.5 ? 'X' : 'O';
    turnElem.innerText = turn;
}

/*
* Ho aggiunto il parametro opzionale dei punti da aggiungere cosí da poterli cheattare.*/
function addPoints(player, quantity=1) {
    if (player === 'X') {
        x += quantity;
        xPoints.innerText = x;
    } else {
        o += quantity;
        oPoints.innerText = o;
    }
}

/*
* Restituisce il simbolo del vincitore se una delle condizioni di vittoria é soddisfatta.
* Restituisce una stringa 'Pareggio' se tutte le caselle sono piene senza una condizione di vittoria.
* Restituisce false negli altri casi.*/
function winCondition() {
    // righe
    if ((box1.innerText === turn && box2.innerText === turn && box3.innerText === turn) ||
        (box4.innerText === turn && box5.innerText === turn && box6.innerText === turn) ||
        (box7.innerText === turn && box8.innerText === turn && box9.innerText === turn) ||

        // colonne
        (box1.innerText === turn && box4.innerText === turn && box7.innerText === turn) ||
        (box2.innerText === turn && box5.innerText === turn && box8.innerText === turn) ||
        (box3.innerText === turn && box6.innerText === turn && box9.innerText === turn) ||

        // diagonali
        (box1.innerText === turn && box5.innerText === turn && box9.innerText === turn) ||
        (box3.innerText === turn && box5.innerText === turn && box7.innerText === turn)) {
        return turn;

    } else if (box1.innerText && box2.innerText && box3.innerText &&
        box4.innerText && box5.innerText && box6.innerText &&
        box7.innerText && box8.innerText && box9.innerText) {
        return 'Pareggio';
    }
    return false
}

/*
* Il parametro all é utile per resettare il punteggio dei due giocatori.
* Resetta il valore di tutti i box con un ciclo for.*/
function reset(all=false) {
    if (all) {
        o = 0;
        x = 0;
        xPoints.innerText = x;
        oPoints.innerText = o;
    }
    for (let i = 1; i <= 9; i++) {
        let elemento = document.getElementById('box' + i);
        elemento.innerText = '';
        elemento.style.color = '#000';
    }
}

/*
* Gestisce i casi di vittoria.
* Non gestisco il caso di winner = false.*/
function checkWinner() {
    const winner = winCondition();
    if (winner === 'X' || winner === 'O') {
        addPoints(winner);
        reset()
    } else if (winner === 'Pareggio') {
        alert(winner);
        reset()
    }
}

/*
* Inverte i turni di gioco.*/
function swapTurn() {
    /*if (turn === 'X') {
        turn = 'O';
    } else {
        turn = 'X';
    }*/
    turn = turn === 'X' ? 'O' : 'X';
    turnElem.innerText = turn;
}

/*
* Cambia il colore dell'elemento in base al valore.*/
function changeColor(elemento) {
    if (elemento.innerText === 'X') {
        elemento.style.color = '#f00';
    } else {
        elemento.style.color = '#00f';
    }
}

/*
* Stampa l'elemento cliccato e il turno corrente.
* Permette di cliccare sulle caselle solo se queste sono vuote.*/
function handleMove(elemento) {
    console.log('É stato premuto il ' + elemento.id + '. Turno: ' + turn);
    if (!elemento.innerText) {
        elemento.innerText = turn;
        changeColor(elemento);
        checkWinner();
        swapTurn();
    }
}