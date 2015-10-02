ref=/mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/MaskN

bwa mem $ref 5a_S5_L001_R1_001.fastq 5a_S5_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o 5a.flt.bam -
bwa mem $ref 5b_S6_L001_R1_001.fastq 5b_S6_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o 5b.flt.bam -
bwa mem $ref S96a_S1_L001_R1_001.fastq S96a_S1_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o S96a.flt.bam -
bwa mem $ref S96b_S2_L001_R1_001.fastq S96b_S2_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o S96b.flt.bam -
bwa mem $ref YJM789a_S3_L001_R1_001.fastq YJM789a_S3_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o YJM789a.flt.bam -
bwa mem $ref YJM789b_S4_L001_R1_001.fastq YJM789b_S4_L001_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T tmp -o YJM789b.flt.bam -

picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=5a.flt.bam OUTPUT=5a.bam REMOVE_DUPLICATES=true  METRICS_FILE=5a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=5b.flt.bam OUTPUT=5b.bam REMOVE_DUPLICATES=true  METRICS_FILE=5b.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=S96a.flt.bam OUTPUT=S96a.bam REMOVE_DUPLICATES=true  METRICS_FILE=S96a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=S96b.flt.bam OUTPUT=S96b.bam REMOVE_DUPLICATES=true  METRICS_FILE=S96b.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=YJM789a.flt.bam OUTPUT=YJM789a.bam REMOVE_DUPLICATES=true  METRICS_FILE=YJM789a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=YJM789b.flt.bam OUTPUT=YJM789b.bam REMOVE_DUPLICATES=true  METRICS_FILE=YJM789b.metrics.txt
