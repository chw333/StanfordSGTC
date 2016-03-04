# coding: utf-8
import pandas as pd
df = pd.read_table('Drug_cell_gene_connection', header=0)

L=[]
for i in range(2,df.shape[1]):
    if 1 not in list(df.ix[1:df.shape[0],i]) and -1 not in list(df.ix[1:df.shape[0],i]):
        L.append(i)
df = df.drop(df.columns[L], 1)
df = df.T
df.to_csv('Drug_cell_gene_connection_Formated',sep='\t', header=None)



