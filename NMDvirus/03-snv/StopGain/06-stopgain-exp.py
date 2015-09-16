import pandas as pd
def stopgain(inF, inF2, S):
    G = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        gene = fields[1]
        ref = int(fields[-2])
        alt = int(fields[-1])
        if sample in S:
            if ref + alt >= 10:
                G[gene] = 'NA'
    inFile.close()

    L = []
    inFile = open(inF2)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        fc = fields[2]
        baseMean = fields[1]
        if fc != 'NA':
            if gene in G and G[gene] == 'NA':
                G[gene] = [float(fc), float(baseMean)]
                L.append(float(fc))
    inFile.close()

    E = pd.DataFrame(L, columns=[inF.split('-')[0]])
    Ex = E.describe()
    print(Ex)


    #for k in G:
    #    print(k + '\t' + str(G[k][0]) + '\t' + str(G[k][1]))





stopgain('HCV-Stopgain-SNV-het-ase', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HCV/deHCV1.txt', ['Mock72-rep1','Mock72-rep2','WTvirus72-rep1','WTvirus72-rep2'])
stopgain('HIV-Stopgain-SNV-het-ase','/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/HIV-1/deHIV1_24h.txt', ['Mock_24-rep1','Mock_24-rep2','HIV_24-rep1','HIV_24-rep2','HIV_24-rep3'])
stopgain('RSV-Stopgain-SNV-het-ase','/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV/deHRSV20h.txt',['HRSV0h-rep1','HRSV0h-rep2','HRSV20h-rep1','HRSV20h-rep2'])
stopgain('KHSV-Stopgain-SNV-het-ase','/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/KHSV/deKHSV.txt',['Mock-rep1','Mock-rep2','Mock-rep3','KHSV-rep1','KHSV-rep2','KHSV-rep3'])
