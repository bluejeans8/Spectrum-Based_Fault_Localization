#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting methods rankings of buggy version#$a"
    cd /usr/Jinseok_SBFL/lang_sbfl_scores
    python get_methods_rankings.py $a
done