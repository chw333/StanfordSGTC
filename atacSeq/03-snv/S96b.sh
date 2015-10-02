#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa S96b.bam | bcftools call -cv - > S96b.raw.vcf 
vcfutils.pl varFilter -d 10 -D 1000 S96b.raw.vcf > S96b.flt.vcf
