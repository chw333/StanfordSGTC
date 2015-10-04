samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock-rep1.bam | bcftools call -cv - > Mock-rep1.raw.vcf 
bcftools view Mock-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock-rep1.flt.vcf
