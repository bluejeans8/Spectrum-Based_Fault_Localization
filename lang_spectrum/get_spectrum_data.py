import sys
from pathlib import Path
from xml.etree.ElementTree import parse
import numpy as np
import pandas as pd
import glob

version_num = sys.argv[1]

files = glob.glob("/usr/Jinseok_SBFL/lang_coverage/all_tests_coverage_data/" + "lang_" + version_num + "_buggy" + '/**/*.xml', recursive = True)
spectrum_dataframes = dict()

# make the base spectrum dataframes
first_file = files[0]
tree = parse(first_file)
classes = tree.findall('./packages/package/classes/class')
for cl in classes:
    spectrum_df = pd.DataFrame([],columns=['entered'])
    methods = cl.findall('./methods/method')
    for method in methods:
        lines = method.findall('./lines/line')
        for line in lines:
            spectrum_df.loc[method.attrib['name'] + ":" + method.attrib['signature'] + ":" + line.attrib['number']] = 0
    spectrum_dataframes[cl.attrib['name']] = spectrum_df

# add values to the spectrum dataframes
for file in files:
    print(file)
    tree = parse(file)
    classes = tree.findall('./packages/package/classes/class')
    for cl in classes:
        spectrum_df = spectrum_dataframes[cl.attrib['name']]
        methods = cl.findall('./methods/method')
        for method in methods:
            lines = method.findall('./lines/line')
            for line in lines:
                if int(line.attrib['hits']) > 0:
                    spectrum_df['entered'][method.attrib['name'] + ":" + method.attrib['signature'] + ":" + line.attrib['number']] += 1

for item in spectrum_dataframes.items():
    filepath = Path('/usr/Jinseok_SBFL/lang_spectrum/lang_' + version_num + '_buggy/' + item[0])
    filepath.parent.mkdir(parents=True, exist_ok=True)
    item[1].to_csv(filepath,index=True)
