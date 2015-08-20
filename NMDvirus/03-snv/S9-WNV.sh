samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S9-WNV.bam | bcftools call -cv - > S9-WNV.raw.vcf 
bcftools view S9-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S9-WNV.flt.vcf
