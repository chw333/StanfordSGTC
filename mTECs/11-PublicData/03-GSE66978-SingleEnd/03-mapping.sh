#read1=SRR2183095_1.fastq.gz
#read2=SRR2183095_2.fastq.gz
#sample=Ren-1
#bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -


read1=SRR2183096_1.fastq.gz
read2=SRR2183096_2.fastq.gz
sample=Ren-2
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR2183097_1.fastq.gz
read2=SRR2183097_2.fastq.gz
sample=Stag2-1
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR2183098_1.fastq.gz
read2=SRR2183098_2.fastq.gz
sample=Stag2-2
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -
