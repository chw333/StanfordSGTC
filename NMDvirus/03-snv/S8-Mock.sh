samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S8-Mock.bam | bcftools call -cv - > S8-Mock.raw.vcf 
bcftools view S8-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S8-Mock.flt.vcf
