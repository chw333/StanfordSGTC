import os
Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.bam':
        raw = F[0:-4] + '.raw.vcf'
        filtered = F[0:-4] + '.flt.vcf'
        ouFile = open(F[0:-4] + '.sh', 'w')
        ouFile.write('#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa %s | bcftools call -cv - > %s \n'%(F, raw))
        #ouFile.write('bcftools view %s |vcfutils.pl varFilter -d 10 -D 500 -a 2 -w 3 -W 10 -1 0.0001 -4 0.0001 > %s\n'%(raw, filtered))
        ouFile.write('vcfutils.pl varFilter -d 10 -D 1000 %s > %s\n'%(raw, filtered))
        ouFile.close()
