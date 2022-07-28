#!/bin/sh

a=0
while [ "$a" -lt 64 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo $a
done
