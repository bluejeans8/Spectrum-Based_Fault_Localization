#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting suspicious classes of buggy version#$a"
    cd /usr/Jinseok_SBFL/lang_classes
    python get_suspicious_classes.py $a
done
