picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139
sample=Lars
INPUT_BAM=${sample}.bam
RD_BAM=${sample}_RD.bam
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=$INPUT_BAM OUTPUT=$RD_BAM REMOVE_DUPLICATES=true  METRICS_FILE=${sample}.metrics.txt
samtools index $RD_BAM







