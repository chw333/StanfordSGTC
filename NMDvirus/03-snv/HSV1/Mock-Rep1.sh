samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock-Rep1.bam | bcftools call -cv - > Mock-Rep1.raw.vcf 
bcftools view Mock-Rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock-Rep1.flt.vcf
