REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19
SAMTOOLS=/mnt/larsix/projects/NMD/hansun/MySoft/samtools/samtools-1.2/samtools

bwa mem -M -t 8 -R '@RG\tID:group1\tSM:sample1\tPL:illumina\tLB:lib1\tPU:unit1' $REF 69-081_R1.fastq.gz 69-081_R2.fastq.gz |$SAMTOOLS view -q 60 -b - | $SAMTOOLS sort -O bam -T Lars.tmp -o Lars.bam -
