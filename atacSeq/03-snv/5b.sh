#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa 5b.bam | bcftools call -cv - > 5b.raw.vcf 
vcfutils.pl varFilter -d 10 -D 1000 5b.raw.vcf > 5b.flt.vcf
