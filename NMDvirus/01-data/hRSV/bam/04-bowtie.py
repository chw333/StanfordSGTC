import os
Fs = os.listdir('.')
ouFile = open('04-bowtie.sh', 'w')
###ouFile2 = open('04-bowtie2.sh', 'w')
for F in Fs:
    if F[-9:] == '.fastq.gz':
        if F[-11:] == '_1.fastq.gz':
            pre = F.split('_1.fastq.gz')[0]
            ###pre_all = pre + '.all'
            ###ouFile.write('tophat --b2-sensitive -p 8 -o %s --transcriptome-index /mnt/larsix/projects/NMD/hansun/Data/Ensembl/tophat2/transcriptome-index/Homo_sapiens.GRCh38 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 %s\n'%(pre, F))
            ouFile.write('bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 %s -2 %s | samtools view -q 30 -bS - | samtools sort - %s\n'%(pre+'_1.fastq.gz', pre+'_2.fastq.gz', pre))
            ###ouFile.write('samtools index %s.bam\n'%(pre))
            ###ouFile2.write('bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 %s -2 %s | samtools view -bS - | samtools sort - %s\n'%(pre + '_1.fastq', pre+'_2.fastq', pre_all))
            ####ouFile2.write('samtools index %s.bam\n'%(pre_all))
        elif F[-11:] == '_2.fastq.gz':
            pass
        else:
            pre = F.split('.fastq.gz')[0]
            ouFile.write('bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U %s | samtools view -q 30 -bS - | samtools sort - %s\n'%(F, pre))
ouFile.close()
###ouFile2.close()

