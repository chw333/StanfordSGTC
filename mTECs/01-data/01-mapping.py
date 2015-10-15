import os

ref='/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome'

Fs = os.listdir('.')
D = {}
for F in Fs:
    if F[-6:] == '.fastq':
        if F.find('_R1_001.fastq') != -1:
            pre = F.split('_R1_001.fastq')[0]
        elif F.find('_R2_001.fastq') != -1:
            pre = F.split('_R2_001.fastq')[0]
        else:
            print('Warning')
        D[pre] = 1
for k in D:
    ouFile = open(k + '.sh', 'w')
    ouFile.write('bwa mem -t 8 %s %s %s |samtools view -q 30 -b - | samtools sort -O bam -T %s -o %s -\n'%(ref, k+'_R1_001.fastq', k+'_R2_001.fastq',k+'.tmp',k+'.bam'))
    ouFile.close()
    
    
