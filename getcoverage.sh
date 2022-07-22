#!/bin/sh

# cnt=0
while read line ; do
    # cnt=$(($cnt + 1))
    # python lang_get_tmp_classes.py $line
    # ret=$?
    # if [ $ret -gt 0 ]
    # then
    #     echo $cnt "pass" $ret $line
    # else
    #     echo "fail"
    #     exit 0
    # fi
    echo "\n[Testing] $line"
    defects4j coverage -w "../../tmp/lang_1_fixed" -t $line -i "lang_classes/lang_all_classes"
    python coverage_parser.py $line
    # cp ../../tmp/lang_1_fixed/coverage.xml coverage_data/$line.xml
done < "lang_tests/parsed_lang_all_tests"