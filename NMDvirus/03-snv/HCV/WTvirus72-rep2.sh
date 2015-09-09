samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa WTvirus72-rep2.bam | bcftools call -cv - > WTvirus72-rep2.raw.vcf 
bcftools view WTvirus72-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > WTvirus72-rep2.flt.vcf
