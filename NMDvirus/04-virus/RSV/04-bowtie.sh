bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV4h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV4h-unmapped-rep1
samtools index HRSV4h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV2h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV2h-unmapped-rep2
samtools index HRSV2h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV4h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV4h-unmapped-rep2
samtools index HRSV4h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV2h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV2h-unmapped-rep1
samtools index HRSV2h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV12h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV12h-unmapped-rep2
samtools index HRSV12h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV8h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV8h-unmapped-rep2
samtools index HRSV8h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV20h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV20h-unmapped-rep1
samtools index HRSV20h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV12h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV12h-unmapped-rep1
samtools index HRSV12h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV20h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV20h-unmapped-rep2
samtools index HRSV20h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV8h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV8h-unmapped-rep1
samtools index HRSV8h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV0h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV0h-unmapped-rep2
samtools index HRSV0h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV0h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV0h-unmapped-rep1
samtools index HRSV0h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV16h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV16h-unmapped-rep1
samtools index HRSV16h-unmapped-rep1.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV24h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV24h-unmapped-rep2
samtools index HRSV24h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV16h-unmapped-rep2.fq | samtools view  -bS - | samtools sort - HRSV16h-unmapped-rep2
samtools index HRSV16h-unmapped-rep2.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U HRSV24h-unmapped-rep1.fq | samtools view  -bS - | samtools sort - HRSV24h-unmapped-rep1
samtools index HRSV24h-unmapped-rep1.bam
