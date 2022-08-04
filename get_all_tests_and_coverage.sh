#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting all tests of buggy version#$a"
    cd /tmp/lang_${a}_buggy
    defects4j compile
    defects4j test
    cd /usr/Jinseok_SBFL/lang_tests
    python get_all_tests.py $a
    mkdir /usr/Jinseok_SBFL/lang_coverage/all_tests_coverage_data/lang_${a}_buggy
    while read line ; do
        echo "\n[Getting coverage] $line"
        defects4j coverage -w /tmp/lang_${a}_buggy -t $line -i /usr/Jinseok_SBFL/lang_classes/suspicious_classes/suspicious_classes#${a}
        cp /tmp/lang_${a}_buggy/coverage.xml /usr/Jinseok_SBFL/lang_coverage/all_tests_coverage_data/lang_${a}_buggy/$line.xml
    done < "/usr/Jinseok_SBFL/lang_tests/all_tests/all_tests#${a}"
done

