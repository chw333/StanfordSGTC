bam=Tspan8_negative_MHCII_high_rep1
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
