class Album {
    constructor () {
        this.songs = [];
    }

    add(song) {
        this.songs.push(song);
        return song;
    }

    remove(song) {
        /*
            Rimuove e restituisce l'ultimo elemento dell'array se non vengono passati parametri.
        */
        if (song === undefined) {
            return this.songs.pop();
        }
        // indexOf restituisce -1 se l'elemento non é presente nell'array.
        const index = this.songs.indexOf(song);
        
        if (index === -1) {
            return;
        }

        const deleted = this.songs.pop(index);
        return deleted;
    }

    getLength() {
        return this.songs.length;
    }

    printSongs(index) {
        if (index !== undefined) {
            if (index < 0 || index > this.getLength()) {
                return "";
            }
            return this.songs[index].printSong();
        }
        let songsContent = "";
        this.songs.forEach((song, index)=> {
            // solo con 1 o piú canzoni
            if (index > 0) {
                songsContent += "<hr>";
            }
            songsContent += song.printSong();
        });
        return songsContent;
    }
}

class Song{
    constructor(title, author, year, genre) {
        // se viene inserita una stringa vuota, viene valutata come falsa.
        // esegue on OR logico e "vince" chi non é falsy.
        this.title = title || "Non inserito";
        this.author = author || "Non inserito";
        this.year = year || "Non inserito";
        this.genre = genre || "Non inserito";
    }

    printSong() {
        // il template mantiene la formattazione che gli si da nel codice.
        return `<div class="song">
                <strong>Titolo</strong>: ${this.title}<br>
                <strong>Autore</strong>: ${this.author}<br>
                <strong>Anno</strong>: ${this.year}<br>
                <strong>Genere</strong>: ${this.genre}
                </div>`;
    }
}

const textElem = document.getElementById("text");
const printNode = document.getElementById("printNode");
const titleElem = document.getElementById("title");
const authorElem = document.getElementById("author");
const yearElem = document.getElementById("year");
const genreSelectElem = document.getElementById("genreSelect");
const addBtn = document.getElementById("addBtn");
const printBtn = document.getElementById("printBtn");
const canzoni = new Album();

addBtn.addEventListener("click", ()=> {
    textElem.textContent = "Canzone aggiunta!";
    canzoni.add(new Song(titleElem.value, authorElem.value, yearElem.value, genreSelectElem.value));
    console.log("canzone aggiunta");
});

printBtn.addEventListener("click", ()=> {
    console.log("stampa");
    if (canzoni.printSongs() === 0) {
        textElem.textContent = "Non ci sono canzoni da visualizzare";
        return;
    } else {
        textElem.textContent = "Canzoni inserite:";
    }
    let a = canzoni.printSongs();
    console.log(a);
    printNode.innerHTML = canzoni.printSongs();
});