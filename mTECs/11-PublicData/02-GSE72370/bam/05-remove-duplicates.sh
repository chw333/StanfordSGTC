picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139

bam=Ren-1_HQ60
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
