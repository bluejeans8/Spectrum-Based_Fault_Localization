import glob

files = glob.glob("../../tmp/lang_1_fixed/src/main/java" + '/**/*.java', recursive = True)
with open('lang_all_classes','w') as wf:
    for file in files:
        index = file.find("org")
        parsed1 = file[index:]
        parsed2 = parsed1.replace("/",".")
        result = parsed2[:-5]
        wf.write(result)
        wf.write('\n')
        