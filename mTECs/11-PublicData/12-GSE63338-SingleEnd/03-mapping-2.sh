read=SRR1653769.fastq.gz
sample=SRR1653769
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653770.fastq.gz
sample=SRR1653770
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653771.fastq.gz
sample=SRR1653771
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653772.fastq.gz
sample=SRR1653772
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653773.fastq.gz
sample=SRR1653773
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653774.fastq.gz
sample=SRR1653774
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

