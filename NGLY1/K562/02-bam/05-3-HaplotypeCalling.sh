GATK=/mnt/larsix/projects/NMD/hansun/MySoft/GATK/GenomeAnalysisTK.jar
REFERENCE=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta


PREPROCESSED_BAM=K562_K15_Recalibrated.bam
RAW_VARIANTS=K562_K15_raw_variants.vcf
java -jar $GATK -T HaplotypeCaller -R $REFERENCE  -I $PREPROCESSED_BAM --genotyping_mode DISCOVERY -stand_emit_conf 10 -stand_call_conf 30 -o $RAW_VARIANTS

