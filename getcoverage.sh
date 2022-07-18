#!/bin/sh

while read line ; do
    defects4j coverage -w "../../tmp/lang_1_fixed" -t $line 
    cp ../../tmp/lang_1_fixed/coverage.xml coverage_data/$line.xml
done < parsed_lang_all_tests