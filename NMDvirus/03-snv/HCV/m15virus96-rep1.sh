#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa m15virus96-rep1.bam | bcftools call -cv - > m15virus96-rep1.raw.vcf 
