#!/bin/bash

directory=$PWD # Prende come directory il percorso in cui si trova il file
# Il comando ( > ) crea un file; il comando ( >> ) scrive su file
> summary.out

# Per ogni sottocartella o file nel percorso preso come parametro
for sub in "$directory"/*; do
  # Se l'elemento è una directory ( -d )
  if test -d "$sub"; then
    name=$(basename "$sub")  # Estrae il nome della cartella
    count=$(ls -1 "$sub" | wc -l)  # ( ls -1 ) mostra i file in una riga alla volta
    echo "La directory '$name' contiene: $count file" >> summary.out  # Scrive la quantità di file nella directory
  # Se l'elemento è un file di testo ( -f )
  elif test -f "$sub"; then
    mime_type=$(file --mime-type -b "$sub")  # Controlla il tipo se il tipo MIME è text/*. tutti i file di testo hanno come MIME text/tipofile
    if [[ "$mime_type" == text/* ]]; then
      name=$(basename "$sub") # Estrae dal percorso il nome del file che ha controllato
      echo "File: $name" >> summary.out  # Scrive il nome del file
      lines=$(wc -l < "$sub")  # Conta le linee del file
      echo "Lines: $lines" >> summary.out  # Scrive il numero di linee
      bytes=$(head -c 10 "$sub")  # Prende i primi 10 byte del file
      echo "Bytes: $bytes" >> summary.out  # Scrive i primi 10 byte
      echo "" >> summary.out  # Aggiunge una riga vuota per separare i file
    else
      echo "File sconosciuto: $sub" >> summary.out  # Se NON sono file di testo
    fi
  else
    echo "Elemento sconosciuto: $sub" >> summary.out  # Se sono file video, audio...
  fi
done
