samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.YJM789.fa S96b.bam | bcftools call -cv - > S96b.raw.vcf 
