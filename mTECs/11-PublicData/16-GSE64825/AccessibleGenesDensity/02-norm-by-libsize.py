import pandas as pd

def norm(inF1, inF2):
    LibSize = pd.read_table(inF1, header=None)
    LibSizeFactor =  20000000

    df = pd.read_table(inF2, header=0) 
    for i in range(4, df.shape[1]):
        df.ix[:,i] = df.ix[:,i]/LibSize.ix[i-4, 1] * LibSizeFactor
    df.to_csv(inF2+'-Norm', sep='\t', index=False)

norm('Mouse-Sample-LibrarySize-NF','Mouse_Gene_Promoter_Cov_ProteinCoding')
norm('Mouse-Sample-LibrarySize-NF-AverRep', 'Mouse_Gene_Promoter_Cov_ProteinCoding-AverRep')



