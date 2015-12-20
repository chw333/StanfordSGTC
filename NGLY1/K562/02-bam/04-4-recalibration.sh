GATK=/mnt/larsix/projects/NMD/hansun/MySoft/GATK/GenomeAnalysisTK.jar
REFERENCE=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta
GOLD_INDEL=/mnt/larsix/projects/NMD/hansun/Data/GATK/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf
DBSNP=/mnt/larsix/projects/NMD/hansun/Data/GATK/dbsnp_138.hg19.vcf


SAMPLE=K562_K20
RECAL_DATA_TABLE=${SAMPLE}.recal_data.table
POST_RECAL_DATA_TABLE=${SAMPLE}.post_recal_data.table
RECAL_PLOTS=${SAMPLE}.recalibration_plots.pdf
REALIGNED_BAM=${SAMPLE}_Realigned.bam
RECALIBRATED_BAM=${SAMPLE}_Recalibrated.bam

java -jar $GATK -T BaseRecalibrator -R $REFERENCE -I $REALIGNED_BAM -knownSites $DBSNP -knownSites $GOLD_INDEL -o $RECAL_DATA_TABLE

java -jar $GATK -T BaseRecalibrator -R $REFERENCE -I $REALIGNED_BAM -knownSites $DBSNP -knownSites $GOLD_INDEL -BQSR $RECAL_DATA_TABLE -o $POST_RECAL_DATA_TABLE

java -jar $GATK -T AnalyzeCovariates -R $REFERENCE -before $RECAL_DATA_TABLE -after $POST_RECAL_DATA_TABLE -plots $RECAL_PLOTS

java -jar $GATK -T PrintReads -R $REFERENCE -I $REALIGNED_BAM -BQSR $RECAL_DATA_TABLE -o $RECALIBRATED_BAM
