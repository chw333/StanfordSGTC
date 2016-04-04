REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19


read1=SRR3048039_1.fastq.gz
read2=SRR3048039_2.fastq.gz
sample=Alpha1
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR3048053_1.fastq.gz
read2=SRR3048053_2.fastq.gz
sample=Acinar3
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

