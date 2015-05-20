#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258470.noN.fastq >SRR1258470.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258471.noN.fastq >SRR1258471.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258533.noN.fastq >SRR1258533.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258534.noN.fastq >SRR1258534.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258535.noN.fastq >SRR1258535.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258536.noN.fastq >SRR1258536.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258537.noN.fastq >SRR1258537.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258538.noN.fastq >SRR1258538.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258539.noN.fastq >SRR1258539.sam

#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258540.noN.fastq >SRR1258540.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258541.noN.fastq >SRR1258541.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258542.noN.fastq >SRR1258542.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258543.noN.fastq >SRR1258543.sam
#bwa mem -a /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast SRR1258544.noN.fastq >SRR1258544.sam

fq=SRR1258539_trimmed
bwa mem /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast ${fq}.fastq | samtools view -bS - -o ${fq}.bam
fq=SRR1258540_trimmed
bwa mem /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast ${fq}.fastq | samtools view -bS - -o ${fq}.bam
fq=SRR1258541_trimmed
bwa mem /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast ${fq}.fastq | samtools view -bS - -o ${fq}.bam
fq=SRR1258542_trimmed
bwa mem /srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/bwa/Yeast ${fq}.fastq | samtools view -bS - -o ${fq}.bam
