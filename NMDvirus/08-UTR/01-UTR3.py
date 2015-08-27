inFile = open('hg38_refGene.txt')
ouFile = open('hg38_refGene_UPF3', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    nm = fields[1]
    ch = fields[2]
    strand = fields[3]
    tx_start = int(fields[4])
    tx_end = int(fields[5])
    cds_start = int(fields[6])
    cds_end = int(fields[7])
    gene = fields[12]
    if nm[0:3] == 'NM_':
        if strand == '+':
            utr3 = tx_end - cds_end
        else:
            utr3 = cds_start - tx_start
        ouFile.write(gene + '\t' + str(utr3) + '\n')

inFile.close()
ouFile.close()
