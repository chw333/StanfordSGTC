#samtools mpileup -uf /mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa 5a.bam | bcftools call -cv - > 5a.raw.vcf 
vcfutils.pl varFilter -d 10 -D 1000 5a.raw.vcf > 5a.flt.vcf
