import pandas as pd

def aver(inF):
    df = pd.read_table(inF, header=0)
    df2 = df.ix[:,[0,1,2,3]].copy()
    df2['Act-B'] = (df['Act-B_rep1'] + df['Act-B_rep2'])/2.0
    df2['Pre-PB'] = (df['Pre-PB_rep1'] + df['Pre-PB_rep2'])/2.0
    df2['PB'] = df['PB_rep1']
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
    for i in range(0, len(L)-1, 2):
        av = (int(L[i][1]) + int(L[i+1][1]))/2
        sample = '_'.join(L[i][0].split('_')[0:-1])
        ouFile.write(sample + '\t' + str(av) + '\n')
    ## for the last one without replicates
    i = len(L)-1
    av = (int(L[i][1]) + int(L[i][1]))/2
    sample = '_'.join(L[i][0].split('_')[0:-1])
    ouFile.write(sample + '\t' + str(av) + '\n')
    ouFile.close()

LibSize('Mouse-Sample-LibrarySize-NF')

