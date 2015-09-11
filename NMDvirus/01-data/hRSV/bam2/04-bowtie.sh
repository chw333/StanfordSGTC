bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1046834_1.fastq.gz -2 SRR1046834_2.fastq.gz | samtools view -q 30 -bS - | samtools sort - SRR1046834
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1046837_1.fastq.gz -2 SRR1046837_2.fastq.gz | samtools view -q 30 -bS - | samtools sort - SRR1046837
