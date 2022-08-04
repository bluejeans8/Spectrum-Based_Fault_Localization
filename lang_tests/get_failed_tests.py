import sys

version_num = sys.argv[1]
with open("/tmp/lang_" + version_num + "_buggy/failing_tests",'r') as rf:
    with open("./failed_tests/" + "failing_tests#" + version_num,'w') as wf:
        for line in rf.readlines():
            if line.startswith("---"):
                wf.write(line[4:])



