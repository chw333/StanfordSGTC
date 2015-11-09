bam=Tspan8_negative_MHCII_high_rep1_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_negative_MHCII_high_rep2_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_negative_MHCII_low_rep1_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_negative_MHCII_low_rep2_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_positive_MHCII_high_rep1_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_positive_MHCII_high_rep2_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_positive_MHCII_low_rep1_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
bam=Tspan8_positive_MHCII_low_rep2_HQ
java -jar /mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139/picard.jar CollectInsertSizeMetrics INPUT=${bam}.bam OUTPUT=${bam}.is HISTOGRAM_FILE=${bam}.pdf
