samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa Mock72-rep2.bam | bcftools call -cv - > Mock72-rep2.raw.vcf 
bcftools view Mock72-rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > Mock72-rep2.flt.vcf
