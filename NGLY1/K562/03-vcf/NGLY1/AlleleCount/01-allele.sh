ref=/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta
bam=K562_WT_Recalibrated.bam
out=K562_WT_Count
bam-readcount -f $ref -l NGLY1-INDEL.bed $bam -w 0 >$out


bam=K562_K8_Recalibrated.bam
out=K562_K8_Count
bam-readcount -f $ref -l NGLY1-INDEL.bed $bam -w 0 >$out


bam=K562_K15_Recalibrated.bam
out=K562_K15_Count
bam-readcount -f $ref -l NGLY1-INDEL.bed $bam -w 0 >$out


bam=K562_K20_Recalibrated.bam
out=K562_K20_Count
bam-readcount -f $ref -l NGLY1-INDEL.bed $bam -w 0 >$out
