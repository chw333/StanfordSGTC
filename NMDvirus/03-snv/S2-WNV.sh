samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S2-WNV.bam | bcftools call -cv - > S2-WNV.raw.vcf 
bcftools view S2-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S2-WNV.flt.vcf
