import os
Fs = os.listdir('.')
ouFile = open('03-tophat.sh', 'w')
for F in Fs:
    if F[-11:] == '_1.fastq.gz':
        pre = F.split('_1.fastq.gz')[0]
        ouFile.write('tophat --b2-sensitive -p 8 -o %s --transcriptome-index /mnt/larsix/projects/NMD/hansun/Data/Ensembl/tophat2/transcriptome-index/Homo_sapiens.GRCh38 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 %s %s\n'%(pre, F.split('_1.fastq.gz')[0] + '_1.fastq.gz', F.split('_1.fastq.gz')[0] + '_2.fastq.gz'))
ouFile.close()

