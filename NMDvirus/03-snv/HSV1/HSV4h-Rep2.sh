samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa HSV4h-Rep2.bam | bcftools call -cv - > HSV4h-Rep2.raw.vcf 
bcftools view HSV4h-Rep2.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > HSV4h-Rep2.flt.vcf
