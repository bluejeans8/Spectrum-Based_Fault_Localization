import glob
import sys

version_num = sys.argv[1]
path = ""
if int(version_num) <= 35:
    path = "/tmp/lang_" + version_num + "_buggy/src/main/java"
else:
    path = "/tmp/lang_" + version_num + "_buggy/src/java"
files = glob.glob(path + '/**/*.java', recursive = True)
with open('/usr/Jinseok_SBFL/lang_classes/all_classes/all_classes#' + version_num,'w') as wf:
    for file in files:
        index = file.find("org")
        parsed1 = file[index:]
        parsed2 = parsed1.replace("/",".")
        result = parsed2[:-5]
        wf.write(result)
        wf.write('\n')
        