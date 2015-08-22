bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S2-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S2-WNV-unmapped
samtools index S2-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S8-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S8-Mock-unmapped
samtools index S8-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S9-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S9-Mock-unmapped
samtools index S9-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S3-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S3-WNV-unmapped
samtools index S3-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S1-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S1-WNV-unmapped
samtools index S1-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S7-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S7-WNV-unmapped
samtools index S7-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S9-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S9-WNV-unmapped
samtools index S9-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S1-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S1-Mock-unmapped
samtools index S1-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S2-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S2-Mock-unmapped
samtools index S2-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S6-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S6-WNV-unmapped
samtools index S6-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S3-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S3-Mock-unmapped
samtools index S3-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S8-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S8-WNV-unmapped
samtools index S8-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S5-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S5-Mock-unmapped
samtools index S5-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S4-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S4-Mock-unmapped
samtools index S4-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S5-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S5-WNV-unmapped
samtools index S5-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S10-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S10-Mock-unmapped
samtools index S10-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S7-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S7-Mock-unmapped
samtools index S7-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S4-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S4-WNV-unmapped
samtools index S4-WNV-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S6-Mock-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S6-Mock-unmapped
samtools index S6-Mock-unmapped.bam
bowtie2 -p 8 -x /mnt/larsix/projects/NMD/hansun/Data/ViralGenomes/ViralGenomes -U S10-WNV-unmapped.fq | samtools view -q 30 -bS - | samtools sort - S10-WNV-unmapped
samtools index S10-WNV-unmapped.bam
