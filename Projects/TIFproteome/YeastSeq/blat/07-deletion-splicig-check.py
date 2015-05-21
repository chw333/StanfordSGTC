def check(inF):
    D = {}
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            D.setdefault(fields[0], [])
            D[fields[0]].append(fields[15])
        else:
            break
    inFile.close()

    inFile = open(inF)
    ouFile = open(inF + '.checked', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')
            pos = fields1[0]
            tp = fields1[15]
            if tp == 'Deletion':
                if 'Splicing' in D[pos]:
                    tp = 'DeletionShouldBeSplicing'
                    ouFile.write('\t'.join(fields1[0:15]) + '\t' + tp + '\t' + '\t'.join(fields1[16:]) + '\n')
                    ouFile.write('\t'.join(fields2[0:15]) + '\t' + tp + '\t' +  '\t'.join(fields2[16:]) + '\n')
                else:
                    ouFile.write(line1 + '\n')
                    ouFile.write(line2 + '\n')
            else:
                ouFile.write(line1 + '\n')
                ouFile.write(line2 + '\n')
        else:
            break
    inFile.close()
    ouFile.close()

check('SRR1258471-soft-filtered.fa.blated.filtered.seq.classified.gene.sorted')
