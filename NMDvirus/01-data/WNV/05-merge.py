inFile = open('SampleInfo.txt')
ouFile = open('05-merge.sh', 'w')
ouFile2 = open('05-merge2.sh', 'w')
D = {}
L = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[2] + '-' + fields[3]
    D.setdefault(k, [])
    D[k].append(fields[0])
    if k not in L:
        L.append(k)
inFile.close()

for k in L:
    ouF = k + '.bam'
    ouF2 = k + '.all.bam'

    s1 = D[k][0] + '.bam'
    s2 = D[k][1] + '.bam'

    s3 = D[k][0] + '.all.bam'
    s4 = D[k][1] + '.all.bam'
    ouFile.write('samtools merge -r -@ 8 %s %s %s\n'%(ouF, s1, s2))
    ouFile.write('samtools index %s\n'%ouF)
    ouFile2.write('samtools merge -r -@ 8 %s %s %s\n'%(ouF2, s3, s4))
    ouFile2.write('samtools index %s\n'%ouF2)

ouFile.close()
ouFile2.close()
