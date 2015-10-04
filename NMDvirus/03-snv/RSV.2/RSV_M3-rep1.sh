samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa RSV_M3-rep1.bam | bcftools call -cv - > RSV_M3-rep1.raw.vcf 
bcftools view RSV_M3-rep1.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > RSV_M3-rep1.flt.vcf
