samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S10-WNV.bam | bcftools call -cv - > S10-WNV.raw.vcf 
bcftools view S10-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S10-WNV.flt.vcf
