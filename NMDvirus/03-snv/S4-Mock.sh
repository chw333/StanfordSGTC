samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S4-Mock.bam | bcftools call -cv - > S4-Mock.raw.vcf 
bcftools view S4-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S4-Mock.flt.vcf
