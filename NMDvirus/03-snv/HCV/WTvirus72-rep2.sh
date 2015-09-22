#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa WTvirus72-rep2.bam | bcftools call -cv - > WTvirus72-rep2.raw.vcf 
