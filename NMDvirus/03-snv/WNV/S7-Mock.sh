samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S7-Mock.bam | bcftools call -cv - > S7-Mock.raw.vcf 
bcftools view S7-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S7-Mock.flt.vcf
