import pandas as pd

def aver(inF):
    df = pd.read_table(inF, header=0)
    df2 = df.ix[:,[0,1,2,3]].copy()
    df2['NrlKO_retina'] = (df['NrlKO_retina_rep1'] + df['NrlKO_retina_rep2'])/2.0
    df2['rd7_retina'] = (df['rd7_retina_rep1'] + df['rd7_retina_rep2'])/2.0
    df2['WT_retina'] = (df['WT_retina_rep1'] + df['WT_retina_rep2'])/2.0
    df2['WT_cones'] = (df['WT_cones_rep1'] + df['WT_cones_rep2'])/2.0
    df2['WT_rods'] = (df['WT_rods_rep1'] + df['WT_rods_rep2'])/2.0
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
        sample = '_'.join(L[i][0].split('_')[0:-1])
        ouFile.write(sample + '\t' + str(av) + '\n')
    ouFile.close()

LibSize('Mouse-Sample-LibrarySize-NF')

