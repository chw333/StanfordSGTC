### one additional column, gene type
RegionLen1 = 2000
RegionLen2 = 1000
inFile = open('Mouse_Gene_Annotation.txt')
ouFile = open('Mouse_Gene_Promoter.gtf', 'w')
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
            promoter_start =  start - RegionLen1
            promoter_end = start - 1 + RegionLen2
            strand = '+'
        elif strand == '-1':
            promoter_start =  end + 1 - RegionLen2
            promoter_end = end + RegionLen1
            strand = '-'
        L.append([ch, str(promoter_start), str(promoter_end), strand, gene])
L.sort(cmp = lambda x,y:cmp(CH.index(x[0]), CH.index(y[0])))
for item in L:
    ouFile.write('\t'.join([item[0], 'FakeGene', 'exon', item[1], item[2], '.', item[3], '0', 'gene_id "%s";'%(item[4]+'_'+item[0]+'_'+item[1]+'_'+item[2])]) + '\n')

    
    
        
inFile.close()
ouFile.close()
