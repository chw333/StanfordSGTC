bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome mouse-ATAC-6_S4_L002_R1_001.fastq mouse-ATAC-6_S4_L002_R2_001.fastq |samtools view -q 30 -b - | samtools sort -O bam -T mouse-ATAC-6_S4_L002.tmp -o mouse-ATAC-6_S4_L002.bam -
