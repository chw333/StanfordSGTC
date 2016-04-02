import pandas as pd

def aver(inF):
    df = pd.read_table(inF, header=0)
    df2 = df.ix[:,[0,1,2,3]].copy()
    df2['Ren'] = (df['Ren-1'] + df['Ren-2'])/2.0
    df2['Stag2'] = (df['Stag2-1'] + df['Stag2-2'])/2.0
    df2.to_csv(inF + '-AverRep', sep='\t', index=False)
aver('Mouse_Gene_Promoter_Cov_ProteinCoding')


def LibSize(inF):
    ouFile = open(inF + '-AverRep', 'w')
    L = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(fields)
    inFile.close()
    for i in range(0, len(L), 2):
        av = (int(L[i][1]) + int(L[i+1][1]))/2
        sample = '_'.join(L[i][0].split('-')[0:-1])
        ouFile.write(sample + '\t' + str(av) + '\n')
    ouFile.close()

LibSize('Mouse-Sample-LibrarySize-NF')

