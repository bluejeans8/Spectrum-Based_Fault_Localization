import sys
from pathlib import Path
from xml.etree.ElementTree import parse
import numpy as np
import pandas as pd


main_df = pd.DataFrame({"class" : [], "line" : [], "hits" : []})
tree = parse('/tmp/lang_1_fixed/coverage.xml')
classes = tree.findall('./packages/package/classes/class')
for cl in classes:
    lines = cl.findall('./methods/method/lines/line')
    for line in lines:
        if(int(line.attrib['hits']) > 0):
            df = pd.DataFrame({"class" : [cl.attrib['name']], "line" : [line.attrib['number']], "hits" : [line.attrib['hits']]})
            main_df = pd.concat([main_df,df], ignore_index=True)

directory_name = sys.argv[1].split('::')[0].split('.')[-1]
file_name = sys.argv[1].split('::')[1].split('.')[0]
filepath = Path('coverage_data/'+ directory_name + '/' + file_name + '.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)  

main_df.to_csv(filepath, index=False)