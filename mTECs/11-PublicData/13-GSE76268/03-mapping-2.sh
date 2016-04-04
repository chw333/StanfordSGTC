REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19

read1=SRR3048047_1.fastq.gz
read2=SRR3048047_2.fastq.gz
sample=Beta2
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR3048049_1.fastq.gz
read2=SRR3048049_2.fastq.gz
sample=Beta3
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR3048051_1.fastq.gz
read2=SRR3048051_2.fastq.gz
sample=Acinar2
bwa mem -t 8 $REF $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -


