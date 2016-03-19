REF=/mnt/larsix/projects/NMD/hansun/Data/Ensembl/tophat2/transcriptome-index/Homo_sapiens.GRCh37
transREF=$REF
#fq1=S635A_1.fastq.gz
#fq2=S635A_2.fastq.gz
#out=S635A
#tophat --b2-sensitive -p 8 -o $out --transcriptome-index $transREF $REF $fq1 $fq2


fq1=CP1_1.fastq.gz
fq2=CP1_2.fastq.gz
out=CP1
tophat --b2-sensitive -p 8 -o $out --transcriptome-index $transREF $REF $fq1 $fq2

fq1=CP2_1.fastq.gz
fq2=CP2_2.fastq.gz
out=CP2
tophat --b2-sensitive -p 8 -o $out --transcriptome-index $transREF $REF $fq1 $fq2
