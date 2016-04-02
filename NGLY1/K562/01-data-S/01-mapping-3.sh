REF=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19
SAMTOOLS=/mnt/larsix/projects/NMD/hansun/MySoft/samtools/samtools-1.2/samtools


read1=H2YG5BBXX_k562_WTgenome_16s000530-1-1_Mueller_lane116s000530_1_sequence.txt.gz
read2=H2YG5BBXX_k562_WTgenome_16s000530-1-1_Mueller_lane116s000530_2_sequence.txt.gz
out=K562_WT
bwa mem -M -t 8 -R '@RG\tID:group3\tSM:WT\tPL:illumina\tLB:lib1\tPU:unit1' $REF $read1 $read2 |$SAMTOOLS view -q 60 -b - | $SAMTOOLS sort -O bam -T ${out}.tmp -o ${out}.bam -
