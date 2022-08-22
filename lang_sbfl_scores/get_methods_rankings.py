import sys

version_num = sys.argv[1]

rank_list = list()
count = 0
with open("/usr/Jinseok_SBFL/lang_sbfl_scores/sbfl_rankings/sbfl_rankings#" + version_num + ".csv",'r') as rf:
    for line in rf.readlines():
        count += 1
        if count == 1:
            continue
        elements = line.split(':')[:-1]
        cl = elements[0]
        method = elements[1]
        signature = elements[2][:(elements[2].find(')'))].replace('(','<') + ">"
        full_string = cl + '$' + method + signature
        if full_string not in rank_list:
            rank_list.append(full_string)

print(rank_list)

with open("/usr/Jinseok_SBFL/lang_sbfl_scores/methods_rankings/methods_rankings#" + version_num + ".csv", 'w') as wf:
    for method in rank_list:
        wf.write(method)
        wf.write('\n')

