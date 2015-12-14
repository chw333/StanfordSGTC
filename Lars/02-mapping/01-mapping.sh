####GATK=/g/steinmetz/hsun/MySoft/GATK/GenomeAnalysisTK.jar
REF=/mnt/larsix/projects/NMD/hansun/Data/Ensembl/bwa/Homo_sapiens.GRCh37
SAMTOOLS=/mnt/larsix/projects/NMD/hansun/MySoft/samtools/samtools-1.2/samtools

bwa mem -M -t 8 -R '@RG\tID:Lars\tSM:Lars' $REF 69-081_R1.fastq.gz 69-081_R2.fastq.gz |$SAMTOOLS view -q 60 -b - | $SAMTOOLS sort -O bam -T Lars.tmp -o Lars.bam -
