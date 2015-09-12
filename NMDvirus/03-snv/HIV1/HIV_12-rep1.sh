samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HIV_12-rep1.bam | bcftools call -cv - > HIV_12-rep1.raw.vcf 
bcftools view HIV_12-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HIV_12-rep1.flt.vcf
