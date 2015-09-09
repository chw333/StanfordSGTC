samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HRSV4h-rep2.bam | bcftools call -cv - > HRSV4h-rep2.raw.vcf 
bcftools view HRSV4h-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HRSV4h-rep2.flt.vcf
