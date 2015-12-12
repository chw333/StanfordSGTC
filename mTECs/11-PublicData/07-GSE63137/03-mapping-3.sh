#read1=SRR1647884_1.fastq.gz
#read2=SRR1647884_2.fastq.gz
#sample=VIP_Neurons_rep1
#bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -


read1=SRR1647885_1.fastq.gz
read2=SRR1647885_2.fastq.gz
sample=VIP_Neurons_rep2
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -
