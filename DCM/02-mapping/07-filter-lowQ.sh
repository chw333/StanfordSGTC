GATK=/mnt/larsix/projects/NMD/hansun/MySoft/GATK/GenomeAnalysisTK.jar
REFERENCE=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta
FILTERED_SNP=Lars_filtered_snp.vcf
FILTERED_INDEL=Lars_filtered_indel.vcf
GQ_FILTERED_SNP=Lars_GQfiltered_snp.vcf
GQ_FILTERED_INDEL=Lars_GQfiltered_indel.vcf

java -jar $GATK -T VariantFiltration -R $REFERENCE -V $FILTERED_SNP -G_filter "GQ < 20.0" -G_filterName lowGQ -o $GQ_FILTERED_SNP
