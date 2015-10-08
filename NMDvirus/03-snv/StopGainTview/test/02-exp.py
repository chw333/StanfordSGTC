G = ['IDI2','WAPAL','FAM63B','DGKE','ZACN','SRA1','KIAA1919','FGL1','HIP1R','PDE4D','NIPBL','STK11','KHDC1','KIAA1161','ZNF14']
def exp(inF, inF2, ouF):
    D = {}
    inFile = open(inF2)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[1]
        D.setdefault(gene, [])
        mock = np.median([float(fields[2]), float(fields[3])])
        virus = np.median([float(fields[4]), float(fields[5])])
        D[gene].append([mock, virus])
    inFile.close()

    inFile = open(inF)
    ouFile = open(ouF, 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        if gene in D:
            #ouFile.write(line + '\t' + str(D[gene][0][0]) + '\t' + str(D[gene][0][1]) + '\n')
            ouFile.write(gene + '\t' + str(D[gene][0][0]) + '\t' + str(D[gene][0][1]) + '\n')
    inFile.close()
    ouFile.close()


#exp('RSV-Stopgain-SNV-gene-formated', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV/geneCounts-HRSV20h-Normalized.txt', 'RSV-Stopgain-SNV-gene-formated-exp')
exp('RSV2-Stopgain-SNV-het-gene', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV.2/geneCounts-RSV_M3-Normalized.txt', 'RSV2_M3-Stopgain-SNV-gene-formated-exp')
#exp('RSV2-Stopgain-SNV-gene-formated', '/mnt/larsix/projects/NMD/hansun/NMDvirus/05-DESeq/RSV.2/geneCounts-RSV_M0.1-Normalized.txt', 'RSV2_M0.1-Stopgain-SNV-gene-formated-exp')
