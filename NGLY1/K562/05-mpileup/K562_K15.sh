samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/Data/Ensembl/bwa/Homo_sapiens.GRCh37.68.dna.chromosomes.withIVTs.fa K562_K15.bam | bcftools call -cv - > K562_K15.raw.vcf 
