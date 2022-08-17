import json
import glob
from pathlib import Path
from xml.etree.ElementTree import parse

buggy_lines_dict = {}

with open('lang_bugs.json', 'r') as rf:
    data = json.load(rf)
    for version in data:
        bugId = version['bugId']
        buggy_lines = []
        changedfile = version["changedFiles"]
        for changes in changedfile:

            changetypes = changedfile[changes]
            for changetype in changetypes:
                lines = changetypes[changetype]
                for line_array in lines:
                    for line in line_array:
                        buggy_lines.append(line)
            buggy_lines_dict[bugId] =  {changes : buggy_lines}

print(buggy_lines_dict)

buggy_methods_dict = {}

for version_num in range(1, 66):
    if version_num != 2:
        buggy_lines = list(buggy_lines_dict[version_num].values())[0]
        dir_path = '/usr/Jinseok_SBFL/lang_coverage/failed_tests_coverage_data/lang_' + str(version_num) + '_buggy/*.*'
        res = glob.glob(dir_path)
        for path in res:
            tree = parse(path)
            classes = tree.findall('./packages/package/classes/class')
            for cl in classes:
                filename = cl.attrib['filename']
                if filename == list(buggy_lines_dict[version_num].keys())[0]:
                    methods = cl.findall('./methods/method')
                    for method in methods:
                        lines = method.findall('./lines/line')
                        min = 100000
                        max = 0
                        for line in lines:
                            if int(line.attrib['number']) < min:
                                min = int(line.attrib['number'])
                            if int(line.attrib['number']) > max:
                                max = int(line.attrib['number'])
                        for bline in buggy_lines:
                            if bline >= min and bline <= max:
                                 buggy_methods_dict[version_num] = {filename : (method.attrib['name'], method.attrib['signature'])}
                                 break



print(buggy_methods_dict)
print((list(buggy_methods_dict.keys())))