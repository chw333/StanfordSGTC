def geno(inF1, inF2):
    D = {}
    inFile = open(inF1)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split()
        k = fields[0] + ':' + fields[1]
        D[k] = 1
    inFile.close()

    inFile = open(inF2)
    ouFile = open(inF2 + '-Ref', 'w')
    head = inFile.readline()
    ouFile.write(head)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        fds = fields[0].split('_')
        k = fds[-2] + ':' + fds[-1]
        if k in D:
            ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

geno('GTEx_genot_imputed_variants_info4_maf05_CR95_CHR_POSb37_ID_REF_ALT.txt', '1000Genome-465LCLs-Genotype-FiltTrans')
