L = []
inFile = open('SampleInfo.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)

inFile.close()

ouFile = open('04-quality-filter.sh', 'w')
for item in L:
    bam = item[0] + '/' + 'accepted_hits.bam'
    SampleName = item[1] + '-' + item[2]
    ouFile.write('samtools view -b %s -q 30 -@ 8 -o %s.bam\n'%(bam, SampleName))
    ouFile.write('samtools index %s.bam\n'%SampleName)
inFile.close()
