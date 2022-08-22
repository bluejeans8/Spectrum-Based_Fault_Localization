acc1 = 0
acc3 = 0
acc5 = 0

for version_num in range(1, 66):
    buggy_methods = list()
    best_rank = 1000
    if version_num != 2:
        with open("/usr/Jinseok_SBFL/lang_buggy_methods/Lang-" + str(version_num), 'r') as cf:
            with open("/usr/Jinseok_SBFL/lang_sbfl_scores/methods_rankings/methods_rankings#" + str(version_num) + ".csv", 'r') as rf:
                for line in cf.readlines():
                    buggy_methods.append(line.strip('\n'))
                rank = 1
                for line in rf.readlines():
                    if line.strip('\n') in buggy_methods:
                        best_rank = rank
                        break
                    rank += 1
    if best_rank <= 5:
        acc5 += 1
    if best_rank <= 3:
        acc3 += 1
    if best_rank == 1:
        acc1 += 1

print("acc@5:", acc5)
print("acc@3:", acc3)
print("acc@1:", acc1)



