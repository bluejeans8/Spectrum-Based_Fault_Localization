import sys

test_name = sys.argv[1].split("::")[0].split(".")[-1]
count = 0

with open('lang_all_classes','r') as rf:
    with open('lang_tmp_classes','w') as wf:
        for line in rf.readlines():
            class_name = line.split(".")[-1][:-1]
            if class_name in test_name:
                wf.write(line)
                count += 1

sys.exit(count)   


    