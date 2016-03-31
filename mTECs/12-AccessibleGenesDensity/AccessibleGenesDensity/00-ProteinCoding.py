D = {}
RegionLen = 1000

inFile = open('Mouse_Gene_Annotation.txt')
head = inFile.readline()
CH = [str(x) for x in range(1, 20)] + ['X', 'Y']
for line in inFile:
    line = line.strip()
    fields = line.split('\t')

    gene_type = fields[6]
    ch = fields[2]
    strand = fields[5]
    start = int(fields[3])
    end = int(fields[4])
    gene = fields[1]

    if strand == '1':
        promoter_start =  start - RegionLen
        promoter_end = start - 1
        strand = '+'
    elif strand == '-1':
        promoter_start =  end + 1
        promoter_end = end + RegionLen
        strand = '-'

    k = '\t'.join([ch, str(promoter_start), str(promoter_end), gene])
    D[k] = gene_type
inFile.close()


inFile = open('mTECs_Gene_Promoter_Cov')
ouFile = open('mTECs_Gene_Promoter_Cov_ProteinCoding', 'w')
head = inFile.readline()
ouFile.write(head)
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join([fields[0], fields[1], fields[2], fields[3]])
    if k in D:
        if D[k] == 'protein_coding':
            ouFile.write(line + '\n')
inFile.close()


