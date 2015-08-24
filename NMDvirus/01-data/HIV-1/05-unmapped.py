L = []
inFile = open('SampleInfo.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)

inFile.close()

ouFile = open('05-unmapped.sh', 'w')
for item in L:
    bam = item[0] + '/' + 'unmapped.bam'
    SampleName = item[1] + '-' + item[2] + '-' + 'unmapped.bam'
    ouFile.write('ln -s %s %s\n'%(bam, SampleName))
inFile.close()
