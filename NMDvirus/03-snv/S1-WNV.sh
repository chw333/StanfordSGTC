samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S1-WNV.bam | bcftools call -cv - > S1-WNV.raw.vcf 
bcftools view S1-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S1-WNV.flt.vcf
