#read1=SRR2183095_1.fastq.gz
#read2=SRR2183095_2.fastq.gz
#sample=Ren-1
#bwa mem -t 8 $REF $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19

read1=SRR891268_1.fastq.gz
read2=SRR891268_2.fastq.gz
sample=GM12878_50k_Rep1
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR891269_1.fastq.gz
read2=SRR891269_2.fastq.gz
sample=GM12878_50k_Rep2
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

