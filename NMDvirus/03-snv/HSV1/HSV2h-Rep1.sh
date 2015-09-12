samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HSV2h-Rep1.bam | bcftools call -cv - > HSV2h-Rep1.raw.vcf 
bcftools view HSV2h-Rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HSV2h-Rep1.flt.vcf
