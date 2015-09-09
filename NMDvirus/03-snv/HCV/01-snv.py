import os
Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.bam':
        raw = F[0:-4] + '.raw.vcf'
        filtered = F[0:-4] + '.flt.vcf'
        ouFile = open(F[0:-4] + '.sh', 'w')
        ouFile.write('samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa %s | bcftools call -cv - > %s \n'%(F, raw))
        ouFile.write('bcftools view %s |vcfutils.pl varFilter -d 5 -D 500 > %s\n'%(raw, filtered))
        ouFile.close()
