GATK=/mnt/larsix/projects/NMD/hansun/MySoft/GATK/GenomeAnalysisTK.jar
REFERENCE=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta
GOLD_INDEL=/mnt/larsix/projects/NMD/hansun/Data/GATK/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf
BAM=Lars_RD.bam
RELIGNMENT_TARGETS=${BAM}.realignment_targets.list
REALIGNED_BAM=Lars_Realigned.bam

java -jar $GATK -T RealignerTargetCreator -R $REFERENCE -I $BAM -known $GOLD_INDEL -o $RELIGNMENT_TARGETS

java -jar $GATK -T IndelRealigner -R $REFERENCE -I $BAM -targetIntervals $RELIGNMENT_TARGETS -known $GOLD_INDEL -o $REALIGNED_BAM
