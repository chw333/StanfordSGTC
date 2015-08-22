samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa S9-Mock.bam | bcftools call -cv - > S9-Mock.raw.vcf 
bcftools view S9-Mock.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > S9-Mock.flt.vcf
