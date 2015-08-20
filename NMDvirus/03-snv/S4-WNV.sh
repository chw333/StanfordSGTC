samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S4-WNV.bam | bcftools call -cv - > S4-WNV.raw.vcf 
bcftools view S4-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S4-WNV.flt.vcf
