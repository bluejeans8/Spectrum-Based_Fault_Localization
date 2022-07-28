import glob
import pandas as pd



with open('./lang_classes/lang_all_classes','r') as rf:
    classes = []
    for line in rf.readlines():
        l = line.strip("\n")
        classes.append(l)
    spectrum_df = pd.DataFrame([],columns=classes)
    

    files = glob.glob("./coverage_data" + '/**/*.csv', recursive = True)
    max = 0
    for file in files:
        df = pd.read_csv(file)
        column = df['line']
        if max < column.max():
            max = column.max()
    for i in range(1,max+1):
        spectrum_df.loc[i] = [0,] * 108
    
    for file in files:
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            cl = row['class'].split('$')[0]
            l = row['line']
            spectrum_df[cl][l] += 1

    spectrum_df.to_csv('lang_spectrumdata.csv',index=True)



    


