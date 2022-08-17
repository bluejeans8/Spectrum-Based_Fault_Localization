import sys

version_num = sys.argv[1]

rank_list = list()
count = 0
with open("/usr/Jinseok_SBFL/lang_sbfl_scores/sbfl_rankings/sbfl_rankings#" + version_num + ".csv",'r') as rf:
    for line in rf.readlines():
        count += 1
        if count == 1:
            continue
        method = ":".join(line.split(':')[:-1])
        if method not in rank_list:
            rank_list.append(method)

with open("/usr/Jinseok_SBFL/lang_sbfl_scores/methods_rankings/methods_rankings#" + version_num + ".csv", 'w') as wf:
    for method in rank_list:
        wf.write(method)
        wf.write('\n')

