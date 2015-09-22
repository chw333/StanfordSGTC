ref=/mnt/larsix/projects/NMD/hansun/atacSeq/00-reference/bwa-index/S288C
bwa mem $ref 5a_S5_L001_R1_001.fastq 5a_S5_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o 5a.bam -
bwa mem $ref 5b_S6_L001_R1_001.fastq 5b_S6_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o 5b.bam -
bwa mem $ref S96a_S1_L001_R1_001.fastq S96a_S1_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o S96a.bam -
bwa mem $ref S96b_S2_L001_R1_001.fastq S96b_S2_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o S96b.bam -
bwa mem $ref YJM789a_S3_L001_R1_001.fastq YJM789a_S3_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o YJM789a.bam -
bwa mem $ref YJM789b_S4_L001_R1_001.fastq YJM789b_S4_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o YJM789b.bam -
