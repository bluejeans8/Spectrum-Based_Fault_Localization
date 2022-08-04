#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting all classes of buggy version#$a"
    cd /usr/Jinseok_SBFL/lang_classes
    python lang_get_all_classes.py $a
done