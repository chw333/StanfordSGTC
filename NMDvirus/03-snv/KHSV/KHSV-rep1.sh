samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa KHSV-rep1.bam | bcftools call -cv - > KHSV-rep1.raw.vcf 
bcftools view KHSV-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > KHSV-rep1.flt.vcf
