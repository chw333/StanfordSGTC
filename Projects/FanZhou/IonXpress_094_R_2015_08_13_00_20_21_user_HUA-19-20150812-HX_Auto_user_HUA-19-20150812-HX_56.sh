samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/UCSC/ucsc-chr/hg19.fa IonXpress_094_R_2015_08_13_00_20_21_user_HUA-19-20150812-HX_Auto_user_HUA-19-20150812-HX_56.bam | bcftools call -cv - > IonXpress_094_R_2015_08_13_00_20_21_user_HUA-19-20150812-HX_Auto_user_HUA-19-20150812-HX_56.raw.vcf 
