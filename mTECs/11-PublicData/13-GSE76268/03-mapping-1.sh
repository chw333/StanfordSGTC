REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19

read1=SRR3048041_1.fastq.gz
read2=SRR3048041_2.fastq.gz
sample=Alpha2
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR3048043_1.fastq.gz
read2=SRR3048043_2.fastq.gz
sample=Alpha3
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR3048045_1.fastq.gz
read2=SRR3048045_2.fastq.gz
sample=Beta1
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

