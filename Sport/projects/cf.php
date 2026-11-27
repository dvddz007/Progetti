<!DOCTYPE html>
<?php
    include "include.php";

    $db = new mysqli($CONFIG["db_host"], $CONFIG["db_user"], $CONFIG["db_pswd"], $CONFIG["db_name"]);
    
    // connect_errno restituisce 0 se non si sono verificati errori.
    if ($db->connect_errno === 0) {
        // La "->" funge da accesso a un metodo di un oggetto.
        // Funziona come il punto in python: obj.metodo()
        echo "Connessione avvenuta con successo." . "<br>";
    } else {
        die("Errore: " . $db->connect_errno);
    }
    
    // da riveredere la result
    $result = db->query("SELECT belfiore FROM comuni WHERE nome=$comune");
?>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calcolatore di codice fiscale</title>
        <link rel="stylesheet" href="../css/cf-style.css">
    </head>
    <body>
        <div id="container">
            <div class="sezione nome">
                <?php
                    echo "Nome: " . ucfirst(strtolower($_POST["nome"]));
                ?>
            </div>
            <div class="sezione cognome">
                <?php
                    echo "Cognome: ";
                    if (str_contains(trim($_POST["cognome"]), " ")) {
                        echo ucfirst(strtolower(explode(" ", $_POST["cognome"])[0])) . " " .  ucfirst(strtolower(explode(" ", $_POST["cognome"])[1]));
                    } else {
                        echo ucfirst(strtolower($_POST["cognome"]));
                    }
                ?>
            </div>
            <div class="sezione data">
                <?php
                    echo "Data di nascità: " . $_POST["dtn"];
                ?>
            </div>
            <div class="sezione sesso">
                <?php
                    echo "Genere: " . strtoupper($_POST["gender"]);
                ?>
            </div>
            <div class="sezione comune">
                <?php
                    echo "Comune di nascità: ";
                    // SELECT nome FROM comuni WHERE nome=$_POST["cdn"]
                    // !(SELECT nome FROM comuni WHERE nome=$_POST["cdn"])
                    
                    $trovato = FALSE;
                    while ($comune = $result->fetch_assoc()) {
                        if ($comune["belfiore"] === $_POST["cdn"]) {
                            echo $comune["nome"];
                            $trovato = TRUE;
                            break;
                        }
                    }
                    if (!$trovato) {
                        echo "Il comune inserito non è presente nel database.";
                    }
                ?>
            </div>
            <?php
                // se tutti i parametri POST sono stati passati e non sono vuoti:
                if (isset($_POST["cognome"], $_POST["nome"], $_POST["dtn"], $_POST["gender"], $_POST["cdn"]) &&
                    validaPOST($_POST["nome"], $_POST["cognome"], $_POST["dtn"], $_POST["gender"], $_POST["cdn"])) {
                    $cf = calcolaCF($_POST["nome"], $_POST["cognome"], $_POST["dtn"], $_POST["cdn"], $_POST["gender"]);
                } else {
                    echo "<div class='sezione'>" . "Uno o più valori inseriti non sono validi o sono mancanti." . "</div>";
                }
            ?>
        </div>
    </body>
</html>
