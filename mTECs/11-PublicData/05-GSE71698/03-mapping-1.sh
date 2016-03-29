#read1=SRR2183095_1.fastq.gz
#read2=SRR2183095_2.fastq.gz
#sample=Ren-1
#bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -


read1=SRR2143368_1.fastq.gz
read2=SRR2143368_2.fastq.gz
sample=Act-B_rep1
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR2143369_1.fastq.gz
read2=SRR2143369_2.fastq.gz
sample=Act-B_rep2
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

