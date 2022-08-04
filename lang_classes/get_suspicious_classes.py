import sys
import glob
from pathlib import Path
from xml.etree.ElementTree import parse

version_num = sys.argv[1]


dir_path = '/usr/Jinseok_SBFL/lang_coverage/failed_tests_coverage_data/lang_' + version_num + '_buggy/*.*'
suspicious_classes = set()

res = glob.glob(dir_path)
for path in res:
    tree = parse(path)
    classes = tree.findall('./packages/package/classes/class')
    for cl in classes:
        lines = cl.findall('./methods/method/lines/line')
        for line in lines:
            if(int(line.attrib['hits']) > 0):
                suspicious_classes.add(cl.attrib['name'].split('$')[0])

with open('/usr/Jinseok_SBFL/lang_classes/suspicious_classes/suspicious_classes#' + version_num, 'w') as wf:
    for cl in suspicious_classes:
        wf.write(cl)
        wf.write('\n')

