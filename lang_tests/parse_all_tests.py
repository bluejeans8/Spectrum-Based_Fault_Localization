with open('lang_all_tests','r') as rf:
    with open('parsed_lang_all_tests','w') as wf:
        for line in rf.readlines():
            s = line.split("(")[1][:-2] + "::" + line.split("(")[0]
            wf.write(s)
            wf.write('\n')

