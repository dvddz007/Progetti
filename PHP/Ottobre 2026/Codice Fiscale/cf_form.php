<!DOCTYPE html>
<?php
    // import del Python.
    include ("config.php");

    // Il quarto parametro dell'oggetto mysqli è facoltativo.
    // $connessione assume un booleano con lo stato di connessione al server.
    $connessione = new mysqli($CONFIG["db_host"], $CONFIG["db_user"], $CONFIG["db_pswd"], $CONFIG["db_name"]);
    
    // connect_errno restituisce 0 se non si sono verificati errori.
    if (!$connessione->connect_errno) {
        // La "->" funge da accesso a un metodo di un oggetto.
        // Funziona come il punto in python: obj.metodo()
        echo "Connessione avvenuta con successo." . "<br>";
    } else {
        die("Errore: " . $connessione->connect_errno);
    }

    // Prende dalla tabella comuni le righe delle colonne "nome" e "belfiore".
    $query = "SELECT nome, belfiore FROM comuni";
    // Invio la query al server.
    $result = $connessione->query($query);
?>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Form</title>
        <link rel="stylesheet" href="cf-style.css">
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
                            // Scorre le righe di $result e assegna l'array a $comune.
                            // L'assegnamento continua finché $comune non é vuota.
                            while ($comune = $result->fetch_assoc()) {
                                // fetch_assoc() continua a prelevare i dati dalla query SQL
                                // assegnando come chiave il nome della colonna
                                // quando non ci sono piú righe, restituisce null.
                                echo '<option value="' . $comune["belfiore"] . '">' . $comune["nome"] . '</option>';
                            }
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