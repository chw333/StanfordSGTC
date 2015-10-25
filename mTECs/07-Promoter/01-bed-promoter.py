RegionLen = 1000
inFile = open('Mouse_Gene_Annotation.txt')
ouFile = open('Mouse_Gene_Promoter.bed', 'w')
CH = [str(x) for x in range(1, 20)] + ['X', 'Y']
head = inFile.readline()
L = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene_type = fields[6]
    ch = fields[2]
    strand = fields[5]
    start = int(fields[3])
    end = int(fields[4])
    gene = fields[1]
    if ch in CH:
        if strand == '1':
            promoter_start =  start - RegionLen
            promoter_end = start - 1
        elif strand == '-1':
            promoter_start =  end + 1
            promoter_end = end + RegionLen
        L.append([ch, str(promoter_start), str(promoter_end), gene])
L.sort(cmp = lambda x,y:cmp(CH.index(x[0]), CH.index(y[0])))
for item in L:
    ouFile.write('\t'.join(item) + '\n')
    
    
        
inFile.close()
ouFile.close()
