samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa KHSV-rep2.bam | bcftools call -cv - > KHSV-rep2.raw.vcf 
bcftools view KHSV-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > KHSV-rep2.flt.vcf
