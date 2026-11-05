<!DOCTYPE html>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calcolatore di codice fiscale</title>
        <link rel="stylesheet" href="cf-style.css">
    </head>
    <body>
        <div id="container">
            <!-- div che racchiude le varie sezioni per centrarlo -->
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
                    echo "Comune di nascità: " . ucfirst(strtolower($_POST["cdn"]));
                ?>
            </div>
            <?php
                /* versione 0.0.2 del 14.10.2026 */
                // http://davidedizio.altervista.org/cf.php?nome=davide&cognome=di%20zio&dtn=15/05/2007&gender=m&cdn=atri

                const VOCALI = ["a", "e", "i", "o", "u"];
                const DATE = [
                    "1" => "a",
                    "2" => "b",
                    "3" => "c",
                    "4" => "d",
                    "5" => "e",
                    "6" => "h",
                    "7" => "l",
                    "8" => "m",
                    "9" => "p",
                    "10" => "r",
                    "11" => "s",
                    "12" => "t"
                ];
                const CARATTERIPARI = [
                    "a" => 0, "0" => 0,
                    "b" => 1, "1" => 1,
                    "c" => 2, "2" => 2,
                    "d" => 3, "3" => 3,
                    "e" => 4, "4" => 4,
                    "f" => 5, "5" => 5,
                    "g" => 6, "6" => 6,
                    "h" => 7, "7" => 7,
                    "i" => 8, "8" => 8,
                    "j" => 9, "9" => 9,
                    "k" => 10,
                    "l" => 11,
                    "m" => 12,
                    "n" => 13,
                    "o" => 14,
                    "p" => 15,
                    "q" => 16,
                    "r" => 17,
                    "s" => 18,
                    "t" => 19,
                    "u" => 20,
                    "v" => 21,
                    "w" => 22,
                    "x" => 23,
                    "y" => 24,
                    "z" => 25
                ];
                const CARATTERIDISPARI = [
                    "a" => 1, "0" => 1,
                    "b" => 0, "1" => 0,
                    "c" => 5, "2" => 5,
                    "d" => 7, "3" => 7,
                    "e" => 9, "4" => 9,
                    "f" => 13, "5" => 13,
                    "g" => 15, "6" => 15,
                    "h" => 17, "7" => 17,
                    "i" => 19, "8" => 19,
                    "j" => 21, "9" => 21,
                    "k" => 2,
                    "l" => 4,
                    "m" => 18,
                    "n" => 20,
                    "o" => 11,
                    "p" => 3,
                    "q" => 6,
                    "r" => 8,
                    "s" => 12,
                    "t" => 14,
                    "u" => 16,
                    "v" => 10,
                    "w" => 22,
                    "x" => 25,
                    "y" => 24,
                    "z" => 23
                ];
                const CARATTERICONTROLLO = [
                    0 => "a",
                    1 => "b",
                    2 => "c",
                    3 => "d",
                    4 => "e",
                    5 => "f",
                    6 => "g",
                    7 => "h",
                    8 => "i",
                    9 => "j",
                    10 => "k",
                    11 => "l",
                    12 => "m",
                    13 => "n",
                    14 => "o",
                    15 => "p",
                    16 => "q",
                    17 => "r",
                    18 => "s",
                    19 => "t",
                    20 => "u",
                    21 => "v",
                    22 => "w",
                    23 => "x",
                    24 => "y",
                    25 => "z"
                ];


                function contaConsonanti(string $stringa): int {
                    $conteggioConsonanti = 0;
                    for ($i=0; $i < strlen($stringa); $i++) {
                        if (!in_array($stringa[$i], VOCALI)) {
                            $conteggioConsonanti++;
                        }
                    }
                    return $conteggioConsonanti;
                }


                function calcolaCognome(string $cognome): string {
                    $cognome = strtolower($cognome);
                    $cognome = str_replace(" ", "", $cognome);
                    $cognome = str_replace("'", "", $cognome);
                    $cognomeCalcolato = "";

                    for ($i=0; $i < strlen($cognome); $i++) {
                        if (!in_array($cognome[$i], VOCALI)) {
                            $cognomeCalcolato .= $cognome[$i];
                            if (strlen($cognomeCalcolato) == 3) {
                                return $cognomeCalcolato;
                            }
                        }
                    }
                    for ($i=0; $i < strlen($cognome); $i++) {
                        if (in_array($cognome[$i], VOCALI)) {
                            $cognomeCalcolato .= $cognome[$i];
                            if (strlen($cognomeCalcolato) == 3) {
                                return $cognomeCalcolato;
                            }
                        }
                    }
                    $cognomeCalcolato .= str_repeat("x", 3 - strlen($cognomeCalcolato));
                    return $cognomeCalcolato;
                }


                function calcolaNome(string $nome): string {
                    $nome = strtolower($nome);
                    $nome = str_replace(" ", "", $nome);
                    $nome = str_replace("'", "", $nome);
                    $nomeCalcolato = "";
                    $counterConsonanti = 0;

                    if (contaConsonanti($nome) < 4) {
                        return calcolaCognome($nome);
                    }
                    for ($i=0; $i < strlen($nome); $i++) {
                        if (!in_array($nome[$i], VOCALI)) {
                            $counterConsonanti++;
                            if ($counterConsonanti == 2) {
                                continue;
                            }
                            $nomeCalcolato .= $nome[$i];
                            if (strlen($nomeCalcolato) == 3) {
                                return $nomeCalcolato;
                            }
                        }
                    }
                    for ($i=0; $i < strlen($nome); $i++) {
                        if (in_array($nome[$i], VOCALI)) {
                            $nomeCalcolato .= $nome[$i];
                            if (strlen($nomeCalcolato) == 3) {
                                return $nomeCalcolato;
                            }
                        }
                    }
                    $nomeCalcolato .= str_repeat("x", 3 - strlen($nomeCalcolato));
                    return $nomeCalcolato;
                }


                function calcolaAnno(string $anno): string {
                    // substr() -> è la slice() (x:y:z) di python.
                    return substr($anno, 2);
                }


                function calcolaMese(string $mese): string {
                    return DATE[(int) $mese];
                }


                function calcolaGiorno(string $giorno, string $sesso): string {
                    if ($sesso == "f") {
                        return (string) ((int) $giorno + 40);
                    }
                    if (strlen($giorno) != 2) {
                        $giorno = "0" . $giorno;
                    }
                    return $giorno;
                }


                function calcolaData(string $data, string $sesso): string {
                    if (!validaData($data)) {
                        return "";
                    }
                    $data = strtolower($data);
                    $sesso = strtolower($sesso);
                    // explode() -> è la split() di python.
                    // explode() restituisce un array.
                    $data = explode("-", $data);
                    $giorno = $data[2];
                    $mese = $data[1];
                    $anno = $data[0];
                    return calcolaAnno($anno) . calcolaMese($mese) . calcolaGiorno($giorno, $sesso);
                }

                
                //function calcolaComune(string $comune): string {
                    /*
                        // ucfirst() -> converte il primo carattere di una stringa in uppercase.
                        $comuni = [];//
                        $righe = file("comuni.txt");

                        foreach ($righe as $riga) {
                            // trim() -> rimuovi caratteri (in questo caso spazi vuoti) ai due estremi della stringa.
                            //
                            // rimuove gli spazi vuoti ai lati e rimuove il tab.
                            array_push($comuni, explode("\t", trim($riga)));
                        }

                        $comune = strtoupper($comune);
                        foreach ($comuni as $c) { 
                            if ($comune == $c[0]) {
                                return str_replace(" ", "", $c[1]);
                            }
                            return "";
                    */
                    /*$comuni = [
                        "ACCIANO" => "A018",
                        "AIELLI" => "A100",
                        "AVEZZANO" => "A515",
                        "CAPESTRANO" => "B651",
                        "L'AQUILA" => "A345",
                        "SULMONA" => "I804",
                        "CHIETI" => "C632",
                        "LANCIANO" => "E435",
                        "VASTO" => "E372",
                        "PESCARA" => "G482",
                        "PENNE" => "G438",
                        "TERAMO" => "L103",
                        "ATRI" => "A488",
                        "GIULIANOVA" => "E058",
                        "ROMA" => "H501"
                    ];

                    $comune = strtoupper(trim($comune));
                    // isset() -> controlla se la variabile (in questo caso la chiave) esiste.
                    if (isset($comuni[$comune])) {
                        return $comuni[$comune];
                    }
                    return "";*/
                    //return $comune;
                //}


                function isBisestile(int $anno): bool {
                    return $anno % 400 == 0 || ($anno % 4 == 0 && $anno % 100 != 0);
                }


                function validaData(string $data): bool {
                    // YYYY-MM-DD
                    if (strlen($data) != 10) {
                        return FALSE;
                    }
                    if ($data[4] != "-" || $data[7] != "-") {
                        return FALSE;
                    }
                    for ($i = 0; $i < strlen($data); $i++) {
                        // salto il controllo quando si scorre su "-".
                        if ($i != 4 && $i != 7) {
                            if (!is_numeric($data[$i])) {
                                return FALSE;
                            }
                        }
                    }
                    $dataL = explode("-", $data);

                    $gg = (int) $dataL[2];
                    $mm = (int) $dataL[1];
                    $aaaa = (int) $dataL[0];

                    $GIORNIMESI = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

                    if ($gg < 1 || $gg > 31 || $mm < 1 || $mm > 12 || $aaaa < 1900 || $aaaa > 2026) {
                        return FALSE;
                    }
                    if ($mm == 2 && isBisestile($aaaa)) {
                        $GIORNIMESI[2] = 29;
                    }
                    if ($gg <= $GIORNIMESI[$mm]) {
                        return TRUE;
                    }
                    return FALSE;
                }


                function letteraControllo(string $cf): string {
                    $cf = strtolower($cf);
                    $somma = 0;
                    for ($i=0; $i < strlen($cf); $i++) {
                        if ($i % 2 == 0) {
                            $somma += CARATTERIDISPARI[$cf[$i]];
                        } else {
                            $somma += CARATTERIPARI[$cf[$i]];
                        }
                    }
                    return CARATTERICONTROLLO[$somma % 26];
                }


                function validaStringa(string $stringa): bool {
                    for ($i=0; $i<strlen($stringa); $i++) {
                        if (is_numeric($stringa[$i])) {
                            return FALSE;
                        }
                    }
                    return TRUE;
                }


                function validaPOST(string $nome, string $cognome, string $data, string $sesso, string $comune): bool {
                    if (trim($nome) == "" || trim($cognome) == "" ||
                        trim($data) == "" || trim($sesso) == "" ||
                        trim($comune) == "") {
                        return FALSE;
                    }
                    if (!validaStringa($nome) || !validaStringa($cognome)) {
                        return FALSE;
                    }
                    if (!validaData($data)) {
                        return FALSE;
                    }

                    if (strtolower($sesso) != "m" && strtolower($sesso) != "f") {
                        return FALSE;
                    }
                    /*if (calcolaComune($comune) == "") {
                        return FALSE;
                    }*/
                    return TRUE;
                }

                // se tutti i parametri POST sono stati passati e non sono vuoti:
               if (isset($_POST["cognome"], $_POST["nome"], $_POST["dtn"], $_POST["gender"], $_POST["cdn"]) &&
                    validaPOST($_POST["nome"], $_POST["cognome"], $_POST["dtn"], $_POST["gender"], $_POST["cdn"])) {
                    $cf = calcolaCognome($_POST["cognome"]) . calcolaNome($_POST["nome"]) .
                        calcolaData($_POST["dtn"], $_POST["gender"]) . $_POST["cdn"];
                    echo "<div class='sezione'>" . strtoupper($cf) . strtoupper(letteraControllo($cf)) . "</div>";
                } else {
                    echo "<div class='sezione'>" . "Uno o più valori inseriti non sono validi o sono mancanti." . "</div>";
                }
            ?>
        </div>
    </body>
</html>
