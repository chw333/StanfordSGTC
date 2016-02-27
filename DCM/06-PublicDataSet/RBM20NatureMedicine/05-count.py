### htseq-count -f bam -s no S1-Mock.bam Homo_sapiens.GRCh38.81.gtf >S1-Mock.count
import os
Fs = os.listdir('.')
ouFile = open('05-count.sh', 'w')
for F in Fs:
    if F[-4:] == '.bam':
        ouF = F.split('.bam')[0] + '.count'
        ouFile.write('htseq-count -f bam -s no %s Homo_sapiens.GRCh37.gff  > %s\n'%(F, ouF))

ouFile.close()
