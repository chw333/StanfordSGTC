import os
Fs = os.listdir('.')
ouFile = open('03-tophat.sh', 'w')
for F in Fs:
    if F[-6:] == '.fastq':
        pre = F.split('.fastq')[0]
        ouFile.write('tophat --b2-sensitive -p 8 -o %s --transcriptome-index /mnt/larsix/projects/NMD/hansun/Data/Ensembl/tophat2/transcriptome-index/Homo_sapiens.GRCh38 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 %s\n'%(pre, F))
ouFile.close()

