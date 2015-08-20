samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S5-Mock.bam | bcftools call -cv - > S5-Mock.raw.vcf 
bcftools view S5-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S5-Mock.flt.vcf
