samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S6-WNV.bam | bcftools call -cv - > S6-WNV.raw.vcf 
bcftools view S6-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S6-WNV.flt.vcf
