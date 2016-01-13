import os
Fs = os.listdir('.')
ouFile = open('04-bowtie.sh', 'w')
#ouFile2 = open('04-bowtie2.sh', 'w')
for F in Fs:
    if F[-9:] == '.fastq.gz':
        pre = F.split('.fastq.gz')[0]
        #pre_all = pre + '.all'
        ouFile.write('tophat --b2-sensitive -p 8 -o %s --transcriptome-index /mnt/larsix/projects/NMD/hansun/Data/Ensembl/tophat2/transcriptome-index/Homo_sapiens.GRCh38 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 %s\n'%(pre, F))
        #ouFile.write('bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U %s | samtools view -q 30 -bS - | samtools sort - %s\n'%(F, pre))
        #ouFile.write('samtools index %s.bam\n'%(pre))
        #ouFile2.write('bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U %s | samtools view -bS - | samtools sort - %s\n'%(F, pre_all))
        #ouFile2.write('samtools index %s.bam\n'%(pre_all))
ouFile.close()
#ouFile2.close()

