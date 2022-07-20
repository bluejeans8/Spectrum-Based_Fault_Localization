from xml.etree.ElementTree import parse

tree = parse('coverage_data/org.apache.commons.lang3.AnnotationUtilsTest::testOneArgNull.xml')
root = tree.getroot()

for child in root:
    for child2 in child:
        print(child2.tag, child2.attrib)
