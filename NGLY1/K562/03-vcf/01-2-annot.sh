ANNOVAR_HUMANDB=/mnt/larsix/projects/NMD/hansun/MySoft/ANNOVAR/annovar/humandb


INPUT_VCF=K562_K15_raw_variants.vcf
OUT=K562_K15
table_annovar.pl $INPUT_VCF $ANNOVAR_HUMANDB -buildver hg19 -out $OUT -remove -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp138,ljb26_all -operation g,r,r,f,f,f,f,f,f,f -nastring . -vcfinput

INPUT_VCF=K562_K20_raw_variants.vcf
OUT=K562_K20
table_annovar.pl $INPUT_VCF $ANNOVAR_HUMANDB -buildver hg19 -out $OUT -remove -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp138,ljb26_all -operation g,r,r,f,f,f,f,f,f,f -nastring . -vcfinput
