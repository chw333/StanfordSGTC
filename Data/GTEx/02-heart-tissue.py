import pandas as pd
def tissue(inF):
    ouFile2 = open(inF.split('.gct')[0] + '_heart_sample', 'w')
    ouFile1 = inF.split('.gct')[0] + '_heart_exp'
    T = {}
    inFile = open('GTEx_Sample2Tissue')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[1].find('Heart') != -1:
            T[fields[0]] = fields[1]
    inFile.close()
    t = T.items()
    t.sort(cmp = lambda x,y:cmp(x[1],y[1]))
    df = pd.read_table(inF, skiprows=2)
    
    S = [df.columns[0], df.columns[1]]

    for x in t:
        if x[0] in df.columns:
            S.append(x[0])
            ouFile2.write(x[0] + '\t' + x[1] + '\n')

    
    G = df[S]
    G.to_csv(ouFile1, sep='\t', index=False)

    ouFile2.close()


    




tissue('GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct')
