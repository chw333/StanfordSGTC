samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock_12-rep3.bam | bcftools call -cv - > Mock_12-rep3.raw.vcf 
bcftools view Mock_12-rep3.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock_12-rep3.flt.vcf
