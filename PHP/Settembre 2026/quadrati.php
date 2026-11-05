<!DOCTYPE html>
<html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            .quadrati {
                width: 100px;
                height: 100px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <?php
                function randomRGB() : int {
                    return mt_rand(0,255);
                }


                /*
                la concatenazione delle stringhe si fa con l'operatore .
                
                str . str é l'equivalente di str + str
                */
                for ($i = 1; $i < 101; $i++) {
                    /*
                    $r = mt_rand(0, 255);
                    $g = mt_rand(0, 255);
                    $b = mt_rand(0, 255);
                    echo "<div class='quadrati' style='background-color: rgb({$r}, {$g}, {$b})'>{$i}</div>";
                    */

                    /*
                    echo "<div class='quadrati' style='background-color: rgb(";
                    echo randomRGB() . "," . randomRGB() . "," . randomRGB();
                    echo ")'>";
                    echo $i;
                    echo "</div>";
                    */

                    echo "<div class='quadrati' style='background-color: rgb("
                    . randomRGB() . "," . randomRGB() . "," . randomRGB() . ")'>"
                    . $i 
                    . "</div>";
                }
            ?>
        </div>
    </body>
</html>