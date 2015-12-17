annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/

annotate_variation.pl -buildver hg19 -downdb cytoBand humandb/

annotate_variation.pl -buildver hg19 -downdb genomicSuperDups humandb/ 

annotate_variation.pl -buildver hg19 -downdb -webfrom annovar esp6500siv2_all humandb/

annotate_variation.pl -buildver hg19 -downdb -webfrom annovar 1000g2014oct humandb/

annotate_variation.pl -buildver hg19 -downdb -webfrom annovar snp138 humandb/ 

annotate_variation.pl -buildver hg19 -downdb -webfrom annovar ljb26_all humandb/

#table_annovar.pl example/ex1.avinput humandb/ -buildver hg19 -out myanno -remove -protocol refGene,cytoBand,genomicSuperDups,esp6500siv2_all,1000g2014oct_all,1000g2014oct_afr,1000g2014oct_eas,1000g2014oct_eur,snp138,ljb26_all -operation g,r,r,f,f,f,f,f,f,f -nastring . -csvout
