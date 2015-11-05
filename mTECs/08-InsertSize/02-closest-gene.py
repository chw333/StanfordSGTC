def gene_annot():
    D = {}
    inFile = open('Mouse_Gene_Annotation_TSS.txt')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        geneID = fields[0]
        geneSym = fields[1]
        ch = fields[2]
        strand = int(fields[5])
        start = int(fields[3])
        end = int(fields[4])
        TSS = fields[-1]
        D.setdefault(ch, [])
        D[ch].append('\t'.join(fields[0:2]+[TSS]+fields[2:]))
    inFile.close()
    return D

def closest_gene(inF):
    D = gene_annot()
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[1]
        pos = fields[2]
        D.setdefault(ch, [])
        D[ch].append(line)
    inFile.close()
    for k in D:
        D[k].sort(cmp = lambda x,y:cmp(int(x.split('\t')[2]), int(y.split('\t')[2])))
    
    inFile = open(inF)
    ouFile = open(inF + '.ClosestGene', 'w')
    for line in inFile:
        line = line.strip()
        ch = line.split('\t')[1]
        if ch in D:
            ind = D[ch].index(line)
            iL = -1
            iR = -1
            for i in range(ind-1,0,-1):
                if D[ch][i].find('ENSMUSG') == 0:
                    left = int(line.split('\t')[2]) - int(D[ch][i].split('\t')[2])
                    iL = i
                    break
            for i in range(ind+1,len(D[ch])):
                if D[ch][i].find('ENSMUSG') == 0: 
                    right = int(D[ch][i].split('\t')[2]) - int(line.split('\t')[2]) 
                    iR = i
                    break
            if iL != -1 and iR != -1:
                if left < right:
                    ouFile.write(line + '\t' + str(left)+'\t' + D[ch][iL] + '\n')
                else:
                    ouFile.write(line + '\t' + str(right) + '\t' + D[ch][iR] + '\n')

    inFile.close()
    ouFile.close()

closest_gene('Tspan8_negative_MHCII_high_rep1.ReadInfo')
