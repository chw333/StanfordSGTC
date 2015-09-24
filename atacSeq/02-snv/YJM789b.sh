samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa YJM789b.bam | bcftools call -cv - > YJM789b.raw.vcf 
