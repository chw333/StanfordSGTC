#samtools rmdup -S 5a.flt.bam        5a.bam
#samtools rmdup -S 5b.flt.bam        5b.bam
#samtools rmdup -S S96a.flt.bam      S96a.bam
#samtools rmdup -S S96b.flt.bam      S96b.bam
#samtools rmdup -S YJM789a.flt.bam   YJM789a.bam
#samtools rmdup -S YJM789b.flt.bam   YJM789b.bam

picard=/mnt/larsix/projects/NMD/hansun/MySoft/picard/picard-tools-1.139
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=5a.flt.bam OUTPUT=5a.bam REMOVE_DUPLICATES=true  METRICS_FILE=5a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=5b.flt.bam OUTPUT=5b.bam REMOVE_DUPLICATES=true  METRICS_FILE=5b.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=S96a.flt.bam OUTPUT=S96a.bam REMOVE_DUPLICATES=true  METRICS_FILE=S96a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=S96b.flt.bam OUTPUT=S96b.bam REMOVE_DUPLICATES=true  METRICS_FILE=S96b.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=YJM789a.flt.bam OUTPUT=YJM789a.bam REMOVE_DUPLICATES=true  METRICS_FILE=YJM789a.metrics.txt
java -Xmx4g -jar $picard/picard.jar MarkDuplicates INPUT=YJM789b.flt.bam OUTPUT=YJM789b.bam REMOVE_DUPLICATES=true  METRICS_FILE=YJM789b.metrics.txt
