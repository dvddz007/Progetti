const strisceElems = document.querySelectorAll(".striscia");
const pulsanteElem = document.getElementById("pulsante");
let timer50ms;
let timer1s;
let i = 0;
let started = true;

pulsanteElem.addEventListener("click", ()=> {
    if (!started) {
        pulsanteElem.value = "START";
        console.log("stop");
        clearInterval(timer1s);
        clearInterval(timer50ms);
        started = true;
    } else {
        console.log("start");
        pulsanteElem.value = "STOP";
        started = false;
        timer1s = setInterval(()=> {
            console.log("1s");
            strisceElems.forEach((striscia)=> {
                striscia.classList.remove("acceso");
            });
            started = false;
            i = 0;
        }, 1000);
        timer50ms = setInterval(()=> {
            console.log("50ms");
            if (i < strisceElems.length){
                strisceElems[i].classList.add("acceso");
                i++;
            }
        }, 50);
    }
});