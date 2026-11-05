#!/bin/bash

echo "Inserire una data in questo formato YYYY/MM/DD: "
read date

year=$(echo $date | cut -d '/' -f1)
month=$(echo $date | cut -d '/' -f2)
day=$(echo $date | cut -d '/' -f3)

mesi=(31 28 31 30 31 30 31 31 30 31 30 31)

source if_bisestile.sh

if [ $(check-bisestile $year) -eq 0 ]; then #condizione con return 1 = mesi[1]=28
mesi[1]=29
else
mesi[1]=28
fi

giorni_totali=0
mese=0

while (( mese < month - 1 )); do
giorni_totali=$((giorni_totali + mesi[mese]))
((mese++))
done

giorni_passati=$((giorni_totali + day))

echo "Sono passati $giorni_passati giorni dall'inizio dell'anno"
