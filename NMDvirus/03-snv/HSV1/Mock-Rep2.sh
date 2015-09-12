samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock-Rep2.bam | bcftools call -cv - > Mock-Rep2.raw.vcf 
bcftools view Mock-Rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock-Rep2.flt.vcf
