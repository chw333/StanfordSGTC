REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19
SAMTOOLS=/mnt/larsix/projects/NMD/hansun/MySoft/samtools/samtools-1.2/samtools


read1=H2YG5BBXX_k562_20genome_16s000532-1-1_Mueller_lane316s000532_1_sequence.txt.gz
read2=H2YG5BBXX_k562_20genome_16s000532-1-1_Mueller_lane316s000532_2_sequence.txt.gz
out=K562_20
bwa mem -M -t 8 -R '@RG\tID:group2\tSM:K20\tPL:illumina\tLB:lib1\tPU:unit1' $REF $read1 $read2 |$SAMTOOLS view -q 60 -b - | $SAMTOOLS sort -O bam -T ${out}.tmp -o ${out}.bam -
