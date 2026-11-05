#!/bin/bash

check-bisestile(year) {
if [[ ($year%4 -eq 0) || ($year%400 -eq 0) ]]; then

echo "$year e' un anno bisestile"
return 0

else

echo "$year non e' un anno bisestile"
return 1

fi
}
