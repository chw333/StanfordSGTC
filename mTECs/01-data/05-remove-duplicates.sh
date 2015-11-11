picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139

bam=Tspan8_negative_MHCII_high_rep1_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_negative_MHCII_high_rep2_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_negative_MHCII_low_rep1_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_negative_MHCII_low_rep2_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_positive_MHCII_high_rep1_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_positive_MHCII_high_rep2_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_positive_MHCII_low_rep1_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=Tspan8_positive_MHCII_low_rep2_HQ
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
