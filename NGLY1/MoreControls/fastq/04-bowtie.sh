bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U dFB_N_03.fastq.gz | samtools view -q 30 -bS - | samtools sort - dFB_N_03
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U dFB_N_02.fastq.gz | samtools view -q 30 -bS - | samtools sort - dFB_N_02
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U dFB_N_01.fastq.gz | samtools view -q 30 -bS - | samtools sort - dFB_N_01
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U WT_D31Y.fastq.gz | samtools view -q 30 -bS - | samtools sort - WT_D31Y
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -U WT_E172D.fastq.gz | samtools view -q 30 -bS - | samtools sort - WT_E172D
