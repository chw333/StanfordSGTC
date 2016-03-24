import os
ouFile = open('Tophat-mapping-filter.sh', 'w')
ouFile2 = open('Tophat-mapping-rm.sh', 'w')
Fs = os.listdir('.')
for F in Fs:
    if F in ['S635A', 'CP1', 'CP2']:
        bam = F + '/' + 'accepted_hits.bam'
        bam_filtered = F + '.bam'
        ouFile.write('samtools view -bh %s -q 50 -o %s\n'%(bam, bam_filtered))
        ouFile.write('rm %s\n'%bam)
        ouFile2.write('rm %s\n'%bam)
ouFile.close()
ouFile2.close()
