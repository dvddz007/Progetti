<?php

$CONFIG["db_host"] = "localhost";
$CONFIG["db_name"] = "sport";
$CONFIG["db_user"] = "root";
$CONFIG["db_pswd"] = "";

$file = __DIR__ . "/comuni.txt";

try {

    // Connessione database
    $pdo = new PDO(
        "mysql:host={$CONFIG['db_host']};dbname={$CONFIG['db_name']};charset=utf8mb4",
        $CONFIG["db_user"],
        $CONFIG["db_pswd"],
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
        ]
    );

    // Verifica esistenza file
    if (!file_exists($file)) {
        throw new Exception("File comuni.txt non trovato!");
    }

    // Inizia transazione
    $pdo->beginTransaction();

    // CANCELLA TUTTI I COMUNI
    $pdo->exec("DELETE FROM comuni");

    // Preparazione query
    $stmt = $pdo->prepare(
        "INSERT INTO comuni (nome, km2, n_abitanti, belfiore)
         VALUES (:nome, 1, 1, :belfiore)"
    );

    // Lettura file
    $righe = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    $inseriti = 0;
    $errori = 0;

    foreach ($righe as $riga) {

        // Divide nome e codice Belfiore
        $dati = preg_split('/\t+/', trim($riga));

        if (count($dati) != 2) {
            $errori++;
            continue;
        }

        $nome = trim($dati[0]);
        $belfiore = trim($dati[1]);

        // Iniziale maiuscola per ogni parola
        $nome = mb_convert_case(
            mb_strtolower($nome, 'UTF-8'),
            MB_CASE_TITLE,
            'UTF-8'
        );

        try {

            $stmt->execute([
                ':nome' => $nome,
                ':belfiore' => $belfiore
            ]);

            $inseriti++;

        } catch (PDOException $e) {
            $errori++;
        }
    }

    // Conferma operazioni
    $pdo->commit();

    // Riepilogo
    echo "<h2>Importazione completata!</h2>";
    echo "Comuni inseriti: " . $inseriti . "<br>";
    echo "Righe con errori: " . $errori . "<br>";

} catch (Exception $e) {

    // Annulla tutto in caso di errore
    if (isset($pdo) && $pdo->inTransaction()) {
        $pdo->rollBack();
    }

    echo "Errore: " . htmlspecialchars($e->getMessage());

}
