import sys

version_num = sys.argv[1]
with open("/tmp/lang_" + version_num + "_buggy/all_tests",'r') as rf:
    with open("./all_tests/" + "all_tests#" + version_num,'w') as wf:
        for line in rf.readlines():
            s = line.split("(")[1][:-2] + "::" + line.split("(")[0]
            wf.write(s)
            wf.write('\n')



