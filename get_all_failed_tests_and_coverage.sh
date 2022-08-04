#!/bin/sh

a=0
while [ "$a" -lt 65 ]
do
    a=$(expr $a + 1)
    if [ "$a" -eq 2 ]
    then
        continue
    fi
    echo "\nGetting failing tests of buggy version#$a"
    defects4j checkout -p Lang -v ${a}b -w /tmp/lang_${a}_buggy
    cd /tmp/lang_${a}_buggy
    defects4j compile
    defects4j test
    cd /usr/Jinseok_SBFL/lang_tests
    python get_failed_tests.py $a
    mkdir /usr/Jinseok_SBFL/lang_coverage/failed_tests_coverage_data/lang_${a}_buggy
    while read line ; do
        echo "\n[Getting coverage] $line"
        defects4j coverage -w /tmp/lang_${a}_buggy -t $line -i /usr/Jinseok_SBFL/lang_classes/all_classes/all_classes#${a}
        cp /tmp/lang_${a}_buggy/coverage.xml /usr/Jinseok_SBFL/lang_coverage/failed_tests_coverage_data/lang_${a}_buggy/$line.xml
    done < "/usr/Jinseok_SBFL/lang_tests/failed_tests/failing_tests#${a}"
done

