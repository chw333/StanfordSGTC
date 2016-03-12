read1=SRR1657634_1.fastq.gz
read2=SRR1657634_2.fastq.gz
sample=SRR1657634
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR1657639_1.fastq.gz
read2=SRR1657639_2.fastq.gz
sample=SRR1657639
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR1657643_1.fastq.gz
read2=SRR1657643_2.fastq.gz
sample=SRR1657643
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR1657644_1.fastq.gz
read2=SRR1657644_2.fastq.gz
sample=SRR1657644
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR1657646_1.fastq.gz
read2=SRR1657646_2.fastq.gz
sample=SRR1657646
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -


