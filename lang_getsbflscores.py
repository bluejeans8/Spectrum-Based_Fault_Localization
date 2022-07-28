# ochiai
import pandas as pd

df_test_list = list()
with open("/tmp/lang_3_buggy/failing_tests",'r') as rf:
    for line in rf.readlines():
        if line.startswith("---"):
            file_name = './coverage_data/' + line.split("::")[0].split(".")[-1] + '/' + line.split("::")[1][:-1] + '.csv'
            df_test = pd.read_csv(file_name)
            df_test_list.append(df_test)

ef_lines = list()
for df_test in df_test_list:
    for index, row in df_test.iterrows():
        cl = row['class'].split('$')[0]
        l = row['line']
        ef_lines.append((cl,l))

df_spectrum = pd.read_csv("./lang_spectrum/lang_spectrumdata.csv")
ep, ef, np, nf = 0, 0, 0, 0 
df_sbfl_score = pd.DataFrame([],columns=['sbfl_score'])

for index, row in df_spectrum.iterrows():
    if index % 1000 == 0:
        print(index)
    for column in df_spectrum:
        if column != 'Unnamed: 0':
            ef = ef_lines.count((column, index+1))
            ep = df_spectrum[column][index] - ef
            nf = len(df_test_list) - ef
            np = 2291 - (ef + ep + nf) 
            if df_spectrum[column][index] == 0:
                ochiai = 0
            else:
                ochiai = ef / ((ef + nf) * (ef + ep))
            if ochiai > 0:
                row_name = column + ":" + str(index)
                df_sbfl_score.loc[row_name] = [ochiai]

print(df_sbfl_score.nlargest(10,'sbfl_score'))



