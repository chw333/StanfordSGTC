picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139

sample=K562_WT
INPUT_BAM=${sample}.bam
RD_BAM=${sample}_RD.bam
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=$INPUT_BAM OUTPUT=$RD_BAM REMOVE_DUPLICATES=true  METRICS_FILE=${sample}.metrics.txt
samtools index $RD_BAM

sample=K562_K8
INPUT_BAM=${sample}.bam
RD_BAM=${sample}_RD.bam
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=$INPUT_BAM OUTPUT=$RD_BAM REMOVE_DUPLICATES=true  METRICS_FILE=${sample}.metrics.txt
samtools index $RD_BAM

sample=K562_K15
INPUT_BAM=${sample}.bam
RD_BAM=${sample}_RD.bam
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=$INPUT_BAM OUTPUT=$RD_BAM REMOVE_DUPLICATES=true  METRICS_FILE=${sample}.metrics.txt
samtools index $RD_BAM

sample=K562_K20
INPUT_BAM=${sample}.bam
RD_BAM=${sample}_RD.bam
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=$INPUT_BAM OUTPUT=$RD_BAM REMOVE_DUPLICATES=true  METRICS_FILE=${sample}.metrics.txt
samtools index $RD_BAM













