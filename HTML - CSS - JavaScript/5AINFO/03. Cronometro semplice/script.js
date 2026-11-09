const showElem = document.getElementById("show");
const stopBtn = document.getElementById("stopBtn");
const startBtn = document.getElementById("startBtn");
let intervalId;
stopBtn.disabled = true;


function start() {
    console.log("start");
    startBtn.disabled = true;
    stopBtn.disabled = false;
    let counterS = 0;
    console.log(counterS);
    intervalId = setInterval( () => {
        counterS++;
        showElem.innerHTML = counterS;
        console.log(counterS);
    }, 1000)
    showElem.innerHTML = counterS;
}


function stop() {
    console.log("stop");
    clearInterval(intervalId);
    startBtn.disabled = false;
    stopBtn.disabled = true;
}
