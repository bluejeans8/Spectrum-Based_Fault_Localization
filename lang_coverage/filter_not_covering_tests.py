import sys
from xml.etree.ElementTree import parse

version_num = sys.argv[1]
tree = parse('/tmp/lang_' + version_num + '_buggy/coverage.xml')
coverage = tree.getroot()
if int(coverage.attrib['lines-covered']) == 0:
    sys.exit(0)
else:
    sys.exit(1)
    


