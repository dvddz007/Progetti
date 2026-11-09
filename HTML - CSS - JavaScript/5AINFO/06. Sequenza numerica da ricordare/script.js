const sequenzaBoxElem = document.getElementById("sequenzaBox");
const testo = document.getElementById("testo");
const sequenzaElem = document.getElementById("sequenza");
const startBtnElem = document.getElementById("startBtn");
const deleteBtnElem = document.getElementById("deleteBtn");
const boxElems = document.querySelectorAll(".box");
// const sequenzaElemArr = sequenzaElem.children;   HTMLCollection != Array
// HTMLCollection non supporta il foreach
//const sequenzaArr = Array.from(sequenzaElem.children);
const sequenzaArr = document.querySelectorAll(".sequenzaNums");
let vinto;
let sequenzaDaIndovinare;
let timerMostra;
let timerIndovina;
let tentativiArr;
let puoCliccare;

function numeroCasuale(min=1, max=3) {
    /*
        Restituisce un numero casuale tra min e max inclusi.
    */
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sequenzaCasuale() {
    /*
        Restituisce un array contenente n numeri casuali da indovinare.
        Si adatta in base a quanti div hanno la classe "sequenzaNums" e restituisce un array con la stessa lunghezza.
    */
    const arr = [];
    for (let i=0; i<sequenzaArr.length; i++) {
        arr.push(numeroCasuale());
    }
    return arr;
}

function salvaTentativo(elemento) {
    /*
        Salva nell'array tentativiArr un elemento SOLO se l'array non supera la lunghezza della sequenza.
    */
    if (tentativiArr.length >= sequenzaDaIndovinare.length) {
        return;
    }
    tentativiArr.push(elemento);
    //return elemento;
    return;
}

function controllaVittoria() {
    /*
        Partendo con vinto = true.
        Scorro simultaneamente l'array dei tentativi e la l'array dei numeri da indovinare.
        Imposta vinto a false se i numeri sono diversi e aggiunge la classe errato al box del numero.
        Aggiunge la classe coretto al box del numero se i numeri comparati sono uguali.
        
    */
    vinto = true;
    for (let i=0; i<sequenzaDaIndovinare.length; i++) {
        if (sequenzaDaIndovinare[i] !== tentativiArr[i]) {
            vinto = false;
            sequenzaArr[i].classList.add("errato");
        } else {
            sequenzaArr[i].classList.add("corretto");
        }
    }
    //vinto = sequenzaDaIndovinare.toString() === tentativiArr.toString();
    return;
}

function mostraSequenzaDaIndovinare() {
    sequenzaArr.forEach((box, index)=> {
        // inserisce nei vari box il numero da indovinare con indice crescente
        box.textContent = String(sequenzaDaIndovinare[index]);
    });
    return;
}

function preparaPartita() {
    // cancello i timer delle partite precedenti
    clearTimeout(timerMostra);
    clearTimeout(timerIndovina);
    testo.textContent = "Ricorda la sequenza:";
    puoCliccare = false;
    tentativiArr = [];
    vinto = false;
    sequenzaDaIndovinare = sequenzaCasuale();
    sequenzaElem.classList.remove("hidden");
    sequenzaElem.classList.remove("vinto", "perso");
    sequenzaArr.forEach((box) => {
        box.classList.remove("corretto", "errato");
    });
}


boxElems.forEach((box)=> {
    box.addEventListener("click", (event)=> {
        // salva il numero cliccato in tentativiArr SE puoi cliccare.
        if (!puoCliccare) {
            return;
        }
        console.log(`cliccato ${event.target.textContent}.`);
        salvaTentativo(Number(event.target.textContent));
        console.log(tentativiArr);
    });
});

deleteBtnElem.addEventListener("click", ()=> {
    if (tentativiArr.length <= 0) {
        console.log("nessun numero da rimuovere.")
        return;
    }
    const x = tentativiArr.pop();
    console.log(`rimosso ${x}.`);
    console.log(tentativiArr);
    return;
})

startBtnElem.addEventListener("click", ()=> {
    startBtnElem.classList.add("hidden");
    preparaPartita();
    mostraSequenzaDaIndovinare();
    console.log("start timer memorizzazione.")
    timerMostra = setTimeout(()=> {
        testo.textContent = "Riproduci la sequenza";
        sequenzaArr.forEach((box) => {
            box.textContent = "?";
        });
        puoCliccare = true;
        deleteBtnElem.classList.remove("hidden");
        console.log("start timer indovino.")
        timerIndovina = setTimeout(()=> {
            puoCliccare = false;
            controllaVittoria();
            mostraSequenzaDaIndovinare();
            setTimeout(() => {
                /*
                    Imposto un timeout di 1ms perchè l'alert è una funzione sincrona;
                    blocca il browser nella sua funzione e non permette la visualizzazione
                    del cambio del textContent degli elementi.
                */
                if (!vinto) {
                    alert("Hai perso!");
                }
                else {
                    alert("Hai vinto!");
                }
            }, 1);
            testo.textContent = "Gioca ancora?"
            startBtnElem.classList.remove("hidden");
            deleteBtnElem.classList.add("hidden");
        }, 5000);
    }, 4000); 
});