samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa m15virus96-rep2.bam | bcftools call -cv - > m15virus96-rep2.raw.vcf 
bcftools view m15virus96-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > m15virus96-rep2.flt.vcf
