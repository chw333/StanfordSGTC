samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HRSV2h-rep2.bam | bcftools call -cv - > HRSV2h-rep2.raw.vcf 
bcftools view HRSV2h-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HRSV2h-rep2.flt.vcf
