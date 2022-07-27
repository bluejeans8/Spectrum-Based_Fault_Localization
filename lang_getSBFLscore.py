# Lang bug 1
import pandas as pd

df_test = pd.read_csv("./coverage_data/NumberUtilsTest/TestLang747.csv")
df_spectrum = pd.read_csv("lang_spectrumdata.csv")
df_sbfl_score = df_spectrum.copy()
ep = 0
ef = 0
np = 0
nf = 0

ef_lines = []
for index, row in df_test.iterrows():
    cl = row['class'].split('$')[0]
    l = row['line']
    ef_lines.append((cl,l))

for index, row in df_spectrum.iterrows():
    for column in df_spectrum:
        if index % 1000 == 0:
            print(index, column)
        if column != 'Unnamed: 0':
            if (column, index+1) in ef_lines:
                ef = 1
                ep = df_spectrum[column][index] - 1
                nf = 0
                np = 2291 - (ef + ep + nf) 
            else:
                ef = 0
                ep = df_spectrum[column][index]
                nf = 1
                np = 2291 - (ef + ep + nf)

            wong2 = ef - ep
            df_sbfl_score[column][index] = wong2
        else:
            df_sbfl_score[column][index] = 0

print(df_sbfl_score.max())

df_sbfl_score.to_csv('lang_wong2_sbfl_score.csv',index=False)






