picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139


bam=Act-B_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt


bam=Act-B_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt



