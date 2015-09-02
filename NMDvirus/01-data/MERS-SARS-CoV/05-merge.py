inFile = open('SampleInfo.txt')
ouFile = open('05-merge.sh', 'w')
D = {}
L = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = fields[1]
    D.setdefault(k, [])
    D[k] += fields[2:]
    if k not in L:
        L.append(k)
inFile.close()


for k in L:
    ouF = k + '.bam'
    if len(D[k]) == 1:
        ouFile.write('mv %s.bam %s\n'%(D[k][0], ouF))
        ouFile.write('samtools index %s\n'%ouF)
    else:
        ouFile.write('samtools merge -r -@ 8 ' + ouF + ' ' + ' '.join([x + '.bam' for x in D[k]]) + '\n')
        ouFile.write('samtools index %s\n'%ouF)

ouFile.close()
