read=SRR1653763.fastq.gz
sample=SRR1653763
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653764.fastq.gz
sample=SRR1653764
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653765.fastq.gz
sample=SRR1653765
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653766.fastq.gz
sample=SRR1653766
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653767.fastq.gz
sample=SRR1653767
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653768.fastq.gz
sample=SRR1653768
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

