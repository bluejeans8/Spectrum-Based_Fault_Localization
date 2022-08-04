#!/bin/sh

a=0
while [ "$a" -lt 64 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting SBFL score ranking of bug#$a"
    defects4j checkout -p Lang -v ${a}b -w /tmp/lang_${a}_buggy
    cd /tmp/lang_${a}_buggy
    defects4j compile
    defects4j test
    cd /usr/Jinseok_SBFL
    python lang_getsbflscores.py $a
done
