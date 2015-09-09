samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock96-rep1.bam | bcftools call -cv - > Mock96-rep1.raw.vcf 
bcftools view Mock96-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock96-rep1.flt.vcf
