# Lang bug 1
import pandas as pd

df_test = pd.read_csv("./coverage_data/NumberUtilsTest/TestLang747.csv")
df_spectrum = pd.read_csv("lang_spectrumdata.csv")
df_sbfl_score = pd.DataFrame([],columns=['sbfl_score'])
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
    if index % 1000 == 0:
        print(index)
    for column in df_spectrum:
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
            if df_spectrum[column][index] == 0:
                ochiai = 0
            else:
                ochiai = ef / ((ef + nf) * (ef + ep))
            if ochiai > 0:
                row_name = column + ":" + str(index)
                df_sbfl_score.loc[row_name] = [ochiai]

print(df_sbfl_score.nlargest(5,'sbfl_score'))

df_sbfl_score.to_csv('lang_ochiai_sbfl_score.csv',index=True)






