samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HRSV0h-rep1.bam | bcftools call -cv - > HRSV0h-rep1.raw.vcf 
bcftools view HRSV0h-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HRSV0h-rep1.flt.vcf
