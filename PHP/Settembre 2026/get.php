<!DOCTYPE html>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <?php
            // http://davidedizio.altervista.org/get.php?nome=davide&cognome=di%20zio&data=15/05/2007&genere=m&comune=atri
            //
            // per indicare i parametri si inizia con un ?
            // più parametri si indicano con la &
            // di default i parametri sono stringhe
            $parametri = var_dump($_GET);
        ?>
    </body>
</html>