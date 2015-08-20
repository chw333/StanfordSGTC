inFile = open('SampleInfo.txt')
ouFile = open('05-merge.sh', 'w')
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
    s1 = D[k][0] + '.bam'
    s2 = D[k][1] + '.bam'
    ouFile.write('samtools merge -r -@ 8 %s %s %s\n'%(ouF, s1, s2))
    ouFile.write('samtools index %s\n'%ouF)

ouFile.close()
