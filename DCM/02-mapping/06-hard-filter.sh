GATK=/mnt/larsix/projects/NMD/hansun/MySoft/GATK/GenomeAnalysisTK.jar
REFERENCE=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta
PREPROCESSED_BAM=Lars_Recalibrated.bam
RAW_VARIANTS=Lars_raw_variants.vcf
RAW_SNP=Lars_raw_snp.vcf
RAW_INDEL=Lars_raw_indel.vcf
FILTERED_SNP=Lars_filtered_snp.vcf
FILTERED_INDEL=Lars_filtered_indel.vcf

java -jar $GATK -T SelectVariants -R $REFERENCE -V $RAW_VARIANTS -selectType SNP -o  $RAW_SNP

java -jar $GATK -T VariantFiltration -R $REFERENCE -V $RAW_SNP --filterExpression "QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0" --filterName "recommended_snp_filter" -o $FILTERED_SNP


java -jar $GATK -T SelectVariants -R $REFERENCE -V $RAW_VARIANTS -selectType INDEL -o  $RAW_INDEL


java -jar $GATK -T VariantFiltration -R $REFERENCE -V $RAW_INDEL --filterExpression "QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0" --filterName "recommended_indel_filter" -o $FILTERED_INDEL

