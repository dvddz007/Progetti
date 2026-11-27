<!DOCTYPE html>
<?php
    // include del C o una specie di import del Python.
    include "include.php";
    include "../config.php";

    // Il quarto parametro dell'oggetto mysqli è facoltativo.
    // $db viene inizializzato come oggetto mysli, che contiene, tra l'altro, lo stato di connessione.
    $db = new mysqli($CONFIG["db_host"], $CONFIG["db_user"], $CONFIG["db_pswd"], $CONFIG["db_name"]);
    
    // connect_errno restituisce 0 se non si sono verificati errori.
    if ($db->connect_errno === 0) {
        // La "->" funge da accesso a un metodo di un oggetto.
        // Funziona come il punto in python: obj.metodo()
        echo "Connessione avvenuta con successo." . "<br>";
    } else {
        die("Errore: " . $db->connect_errno);
    }
?>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form</title>
        <link rel="stylesheet" href="../css/cf-style.css">
    </head>
    <body>
        <div id="container">
            <form id="form" action="cf.php" method="post">
                <div class="sezione nome">
                    <label>Nome:</label>
                    <input type="text" name="nome">
                </div>
                <div class="sezione cognome">
                    <label>Cognome:</label>
                    <input type="text" name="cognome">
                </div>
                <div class="sezione data">
                    <label>Data di nascita:</label>
                    <input type="date" name="dtn">
                </div>
                <div class="sezione sesso">
                    <label>Sesso:</label>
                    <input type="radio" name="gender" value="M">
                    <label>M</label>
                    <input type="radio" name="gender" value="F">
                    <label>F</label>
                </div>
                <div class="sezione comune">
                    <label>Comune di nascita:</label>
                    <select id="cdn" name="cdn">
                        <?php
                            cercaComuni($db);
                        ?>
                    </select>
                </div>
            </form>
            <div class="sezione invio">
                <input type="submit" value="Invia" form="form">
            </div>
        </div>
    </body>
</html>