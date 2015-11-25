bam=K562_WT
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
