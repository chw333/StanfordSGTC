samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S3-WNV.bam | bcftools call -cv - > S3-WNV.raw.vcf 
bcftools view S3-WNV.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S3-WNV.flt.vcf
