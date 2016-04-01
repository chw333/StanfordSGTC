import pandas as pd

df = pd.read_table('mTECs_Gene_Promoter_Cov_ProteinCoding', header=0)
df2 = df.ix[:,[0,1,2,3]].copy()
df2['Tspan8_negative_MHCII_low'] = (df['Tspan8_negative_MHCII_low_rep1'] + df['Tspan8_negative_MHCII_low_rep2'])/2.0
df2['Tspan8_negative_MHCII_high'] = (df['Tspan8_negative_MHCII_high_rep1'] + df['Tspan8_negative_MHCII_high_rep2'])/2.0
df2['Tspan8_positive_MHCII_low'] = (df['Tspan8_positive_MHCII_low_rep1'] + df['Tspan8_positive_MHCII_low_rep2'])/2.0
df2['Tspan8_positive_MHCII_high'] = (df['Tspan8_positive_MHCII_high_rep1'] + df['Tspan8_positive_MHCII_high_rep2'])/2.0
df2.to_csv('mTECs_Gene_Promoter_Cov_ProteinCoding-AverRep', sep='\t', index=False)


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

LibSize('mTECs-Sample-LibrarySize-NF')

