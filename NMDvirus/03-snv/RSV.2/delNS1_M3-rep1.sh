samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa delNS1_M3-rep1.bam | bcftools call -cv - > delNS1_M3-rep1.raw.vcf 
bcftools view delNS1_M3-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > delNS1_M3-rep1.flt.vcf
