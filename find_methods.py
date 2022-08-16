import json
import glob
from pathlib import Path
from xml.etree.ElementTree import parse

# dir_path = '/usr/Jinseok_SBFL/lang_coverage/failed_tests_coverage_data/lang_' + version_num + '_buggy/*.*'
# suspicious_classes = set()

# res = glob.glob(dir_path)
# for path in res:
#     tree = parse(path)
#     classes = tree.findall('./packages/package/classes/class')
#     for cl in classes:
#         lines = cl.findall('./methods/method/lines/line')
#         for line in lines:
            



buggy_lines_dict = {}

with open('lang_bugs.json', 'r') as rf:
    data = json.load(rf)
    for version in data:
        buggy_lines = []
        changedfile = version["changedFiles"]
        for changes in changedfile:
            changetypes = changedfile[changes]
            for changetype in changetypes:
                lines = changetypes[changetype]
                for line_array in lines:
                    for line in line_array:
                        buggy_lines.append(line)
        buggy_lines_dict[version['bugId']] =  buggy_lines


print(buggy_lines_dict)

