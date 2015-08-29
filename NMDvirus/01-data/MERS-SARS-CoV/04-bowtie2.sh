bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192371_1.fastq -2 SRR1192371_2.fastq | samtools view -bS - | samtools sort - SRR1192371.all
samtools index SRR1192371.all.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192370_1.fastq -2 SRR1192370_2.fastq | samtools view -bS - | samtools sort - SRR1192370.all
samtools index SRR1192370.all.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192353_1.fastq -2 SRR1192353_2.fastq | samtools view -bS - | samtools sort - SRR1192353.all
samtools index SRR1192353.all.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bowtie2/Homo_sapiens.GRCh38 -1 SRR1192354_1.fastq -2 SRR1192354_2.fastq | samtools view -bS - | samtools sort - SRR1192354.all
samtools index SRR1192354.all.bam
