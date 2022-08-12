# ochiai
import sys
import pandas as pd
import glob

version_num = sys.argv[1]

all_tests_cnt = 0
with open("/usr/Jinseok_SBFL/lang_tests/all_tests/all_tests#" + version_num,'r') as rf:
    for line in rf.readlines():
        all_tests_cnt += 1

failed_tests_cnt = 0
with open("/usr/Jinseok_SBFL/lang_tests/failed_tests/failing_tests#" + version_num,'r') as rf:
    for line in rf.readlines():
        failed_tests_cnt += 1


files = glob.glob("/usr/Jinseok_SBFL/lang_spectrum/spectrum_data/" + "lang_" + version_num + "_buggy" + '/**/*.csv', recursive = True)

df_sbfl_score = pd.DataFrame([],columns=['sbfl_score'])
ep, ef, np, nf = 0, 0, 0, 0
for file in files:
    df_spectrum = pd.read_csv(file, index_col=[0])
    for index, row in df_spectrum.iterrows():
        ef = row['ef']
        ep = row['ep']
        nf = failed_tests_cnt - ef
        np = all_tests_cnt - (ep + ef + nf)
        if ep + ef == 0:
            ochiai = 0
        else:
            ochiai = ef / ((ef + nf) * (ef + ep))

        if ochiai > 0:
            df_sbfl_score.loc[index] = [ochiai]

sbfl_score_df = df_sbfl_score.sort_values(by ='sbfl_score', ascending = False)
sbfl_score_df.index.name = 'class:method:signature:line'
sbfl_score_df.to_csv('/usr/Jinseok_SBFL/lang_sbfl_scores/sbfl_rankings/sbfl_rankings#'+version_num+'.csv',index=True)


