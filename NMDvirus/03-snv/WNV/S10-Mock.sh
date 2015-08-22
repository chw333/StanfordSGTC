samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S10-Mock.bam | bcftools call -cv - > S10-Mock.raw.vcf 
bcftools view S10-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S10-Mock.flt.vcf
