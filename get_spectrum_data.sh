#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting spectrum data of buggy version#$a"
    cd /usr/Jinseok_SBFL/lang_spectrum
    python get_spectrum_data.py $a
done

