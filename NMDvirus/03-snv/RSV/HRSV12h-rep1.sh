samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HRSV12h-rep1.bam | bcftools call -cv - > HRSV12h-rep1.raw.vcf 
bcftools view HRSV12h-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HRSV12h-rep1.flt.vcf
