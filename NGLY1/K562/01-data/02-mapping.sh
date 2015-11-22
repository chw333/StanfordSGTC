####GATK=/g/steinmetz/hsun/MySoft/GATK/GenomeAnalysisTK.jar
REF=/g/steinmetz/hsun/Stanford3/K562/00-reference/Homo_sapiens.GRCh37
SAMTOOLS=/g/steinmetz/hsun/MySoft/samtools/samtools-1.2/samtools

#bwa mem -M -t 8 -R '@RG\tID:group1\tSM:WT' $REF H2LM7BBXX_k562_WT_15s014311-1-2_Mueller_lane115s014311_1_sequence.txt.gz H2LM7BBXX_k562_WT_15s014311-1-2_Mueller_lane115s014311_2_sequence.txt.gz   |$SAMTOOLS view -q 30 -b - | $SAMTOOLS sort -O bam -T K562_WT.tmp -o K562_WT.bam -

bwa mem -M -t 8 -R '@RG\tID:group2\tSM:K15' $REF H2LM7BBXX_k562_15_15s014313-1-2_Mueller_lane515s014313_1_sequence.txt.gz H2LM7BBXX_k562_15_15s014313-1-2_Mueller_lane515s014313_2_sequence.txt.gz   |$SAMTOOLS view -q 30 -b - | $SAMTOOLS sort -O bam -T K562_K15.tmp -o K562_K15.bam -
#bwa mem -M -t 8 -R '@RG\tID:group2\tSM:K20' $REF H2LM7BBXX_k562_20_15s014314-1-2_Mueller_lane715s014314_1_sequence.txt.gz H2LM7BBXX_k562_20_15s014314-1-2_Mueller_lane715s014314_2_sequence.txt.gz   |$SAMTOOLS view -q 30 -b - | $SAMTOOLS sort -O bam -T K562_K20.tmp -o K562_K20.bam -
#bwa mem -M -t 8 -R '@RG\tID:group2\tSM:K8' $REF H2LM7BBXX_k562_8_15s014312-1-2_Mueller_lane315s014312_1_sequence.txt.gz H2LM7BBXX_k562_8_15s014312-1-2_Mueller_lane315s014312_2_sequence.txt.gz   |$SAMTOOLS view -q 30 -b - | $SAMTOOLS sort -O bam -T K562_K8.tmp -o K562_K8.bam -

