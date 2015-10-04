samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa RSV_M0.1-rep1.sec.bam | bcftools call -cv - > RSV_M0.1-rep1.sec.raw.vcf 
bcftools view RSV_M0.1-rep1.sec.raw.vcf |vcfutils.pl varFilter -d 5 -D 500 > RSV_M0.1-rep1.sec.flt.vcf
