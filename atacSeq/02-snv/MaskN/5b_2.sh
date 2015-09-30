#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.maskN.fa 5b.bam | bcftools call -cvM - > 5b.raw.vcf 
#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.maskN.fa 5b.bam | bcftools call -cAM - > 5b.raw2.vcf 
samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.maskN.fa 5b.bam >5b.mpileup
