### htseq-count -f bam -s no %s Homo_sapiens.GRCh38.81.gtf > %s\n'%(F, ouF)

inFile = open('01-download.sh')
ouFile = open('02-download_count.sh', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('/')
    bam = fields[-1]
    ouF = bam.split('.bam')[0] + '.count'
    ouFile.write(line + '\n')
    #ouFile.write('samtools index ' + bam + '\n')
    ouFile.write('htseq-count -f bam -s no -a 30 %s Homo_sapiens.GRCh37.75.chr.gtf >%s\n'%(bam, ouF))
    ouFile.write('rm ' + bam + '\n')
    #ouFile.write('rm ' + bam + '.bai' + '\n')
inFile.close()
ouFile.close()


