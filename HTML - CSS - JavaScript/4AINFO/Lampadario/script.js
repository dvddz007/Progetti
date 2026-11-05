const contenitore = document.querySelector(".lampadine");       // prendo il contenitore delle lampadine
const lampadine = contenitore.children;     // creo una lista con tutti i figli del contenitore

let stato = 0;      // stato della sequenza
const stati = [
    ["accesa.png", "spenta.png", "spenta.png"],     // solo prima
    ["spenta.png", "accesa.png", "spenta.png"],     // solo seconda
    ["spenta.png", "spenta.png", "accesa.png"],     // solo terza
    ["accesa.png", "accesa.png", "spenta.png"],     // prima + seconda
    ["spenta.png", "accesa.png", "accesa.png"],     // seconda + terza
    ["accesa.png", "spenta.png", "accesa.png"]      // prima + terza
];


function spegni() {
    for (let i = 0; i < lampadine.length; i++) {
        lampadine[i].src = 'spenta.png';
    }
}


function accendi() {
    for (let i = 0; i < lampadine.length; i++) {
        lampadine[i].src = 'accesa.png';
    }
}

function sequenza() {
    for (let i = 0; i < stati[stato].length; i++) {
        lampadine[i].src = stati[stato][i];
    }
    stato++;        // passo allo stato successivo
    
    if (stato >= stati.length) {
        // se ho finito gli stati da controllare:
        stato = 0;      // ripeto al sequenza di stati da capo
    }
}
