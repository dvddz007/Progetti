const startBtn = document.getElementById("startBtn");
const intermedioBtn = document.getElementById("intermedioBtn");
const hhElem = document.getElementById("hh");
const mmElem = document.getElementById("mm");
const ssElem = document.getElementById("ss");
let intervalSId;
let timeoutId;
let counterS = 0;
let counterM = 0;
let counterH = 0;
intermedioBtn.disabled = true;


function start() {
    console.log("start");
    startBtn.disabled = true;
    intermedioBtn.disabled = false;
    console.log(counterS);
    intervalSId = setInterval(()=> {
        counterS++;
        console.log(counterS);
        if (counterS === 60) {
            counterS = 0;
            counterM++;
            ssElem.innerHTML = 0;
        }
        if (counterM === 60) {
            counterM = 0;
            counterH++;
            mmElem.innerHTML = counterM;
        }
        if (counterS < 10) {
            ssElem.innerHTML = "0" + String(counterS);
        } else {
            ssElem.innerHTML = counterS;
        }
        if (counterM < 10) {
                mmElem.innerHTML = "0" + String(counterM);
        } else {
            mmElem.innerHTML = counterM;
        }
        if (counterH < 10) {
                hhElem.innerHTML = "0" + String(counterH);
        } else {
            hhElem.innerHTML = counterM;
        }
    }, 1)
}


function intermedio() {
    console.log("intermedio");
    clearInterval(intervalSId);
    let timeoutId = setTimeout( ()=> {
        counterS += 5;
        start();
    }, 5000)
    startBtn.disabled = false;
    intermedioBtn.disabled = true;
}