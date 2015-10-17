import os
D = {}
Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.bam':
        k = '_'.join(F.split('_')[0:-1])
        D[k] = 1

ouFile = open('02-merge.sh', 'w')
for k in D:
    ouFile.write('samtools merge %s.bam %s %s\n'%(k, k+'_L001.bam', k+'_L002.bam'))
ouFile.close()
