#!/bin/bash

calcolo() {
        data=$(date -d "$year-01-01 +$((num-1)) days" "+%d/%m/%Y")
echo $data
}

year=$(date +%Y)

echo "Inserire un numero"
read num

while [ $num -ge 367 ] || [ $num -le 0 ]; do
	echo "Il numero deve essere compreso tra 1 e 366"
	read num
done
echo "Il numero corrisponde a $(calcolo)"

