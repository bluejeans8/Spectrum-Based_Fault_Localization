#!/bin/sh

a=0
while [ "$a" -lt 1 ]
# getting only first buggy version
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
        cd /usr/Jinseok_SBFL/lang_coverage
        python filter_not_covering_tests.py $a
        if [ "$?" -eq 0 ]
        then
            echo "\n$line : no covered lines" 
            continue
        else
            cp /tmp/lang_${a}_buggy/coverage.xml /usr/Jinseok_SBFL/lang_coverage/all_tests_coverage_data/lang_${a}_buggy/$line.xml
        fi
    done < "/usr/Jinseok_SBFL/lang_tests/all_tests/all_tests#${a}"
done

