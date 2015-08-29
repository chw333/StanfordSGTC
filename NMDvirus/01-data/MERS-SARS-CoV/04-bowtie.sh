bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192371_1.fastq -2 SRR1192371_2.fastq | samtools view -q 30 -bS - | samtools sort - SRR1192371
samtools index SRR1192371.bam
#bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192370_1.fastq -2 SRR1192370_2.fastq | samtools view -q 30 -bS - | samtools sort - SRR1192370
#samtools index SRR1192370.bam
#bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192353_1.fastq -2 SRR1192353_2.fastq | samtools view -q 30 -bS - | samtools sort - SRR1192353
#samtools index SRR1192353.bam
#bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192354_1.fastq -2 SRR1192354_2.fastq | samtools view -q 30 -bS - | samtools sort - SRR1192354
#samtools index SRR1192354.bam
