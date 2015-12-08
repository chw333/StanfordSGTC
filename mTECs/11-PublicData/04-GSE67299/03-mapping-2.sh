read1=SRR1930171_1.fastq.gz
read2=SRR1930171_2.fastq.gz
sample=SRR1930171
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read1=SRR1930173_1.fastq.gz
read2=SRR1930173_2.fastq.gz
sample=SRR1930173
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read1 $read2 |samtools view -q 30 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -
