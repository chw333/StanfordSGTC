read=SRR1653775.fastq.gz
sample=SRR1653775
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653776.fastq.gz
sample=SRR1653776
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653777.fastq.gz
sample=SRR1653777
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653778.fastq.gz
sample=SRR1653778
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -

read=SRR1653780.fastq.gz
sample=SRR1653780
bwa mem -t 8 /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/MouseGenome $read |samtools view -q 60 -b - | samtools sort -O bam -T ${sample}.tmp -o ${sample}.bam -
