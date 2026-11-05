function show() {
    let footer = document.getElementById("footer");
    footer.style.display = "block";
}

function hide() {
    let footer = document.getElementById("footer");
    footer.style.display = "none";
}

// aggiunge all'evento "click" l'esecuzione di una delle due funzioni //
document.getElementById("info").addEventListener("click", function () {
    let footer = document.getElementById("footer");
    /* controllo se non c'Ã¨ un display perchÃ¨
     quando viene caricata per la prima volta la pagina non trova lo stile */
    if (footer.style.display === "none" || footer.style.display === "") {
        show();
    }
    else {
        hide();
    }
})