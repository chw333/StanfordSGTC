picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139

bam=NrlKO_retina_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=NrlKO_retina_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=rd7_retina_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=rd7_retina_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_cones_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_cones_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_retina_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_retina_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_rods_rep1
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
bam=WT_rods_rep2
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=${bam}.bam OUTPUT=${bam}_RD.bam REMOVE_DUPLICATES=true  METRICS_FILE=${bam}.metrics.txt
