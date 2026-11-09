const avantiBtn = document.getElementById("avanti");
const indietroBtn = document.getElementById("indietro");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const imgElem = document.getElementById("immagine");
const imgCount = document.getElementById("imgCount");

const immagini = ["1.png", "2.png", "3.png", "4.png", "5.png"];
stopBtn.disabled = true;
let i = 0;
let timerID;

function avanti() {
    i++;
    if (i > immagini.length) {
        i = 0;
    }
    imgElem.src = `img/${i}.png`;
    imgCount.innerHTML = `Immagine n.${i + 1}`;
}

avantiBtn.addEventListener("click", avanti);

indietroBtn.addEventListener("click", ()=> {
    i--;
    if (i < 0) {
        i = immagini.length - 1;
    }
    imgElem.src = `img/${i}.png`;
    imgCount.innerHTML = `Immagine n.${i + 1}`;
});

startBtn.addEventListener("click", ()=> {
    stopBtn.disabled = false;
    startBtn.disabled = true;
    timerID = setInterval(avanti, 3000);
});

stopBtn.addEventListener("click", ()=> {
    stopBtn.disabled = true;
    startBtn.disabled = false;
    clearInterval(timerID);
});