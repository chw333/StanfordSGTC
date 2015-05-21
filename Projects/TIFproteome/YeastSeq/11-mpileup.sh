ref=/srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa

#bam=SRR1258539_trimmed.sorted
#samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup
#
#bam=SRR1258540_trimmed.sorted
#samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup
#
#bam=SRR1258541_trimmed.sorted
#samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup
#
#bam=SRR1258542_trimmed.sorted
#samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup


bam=SRR1258533.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258534.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258535.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258536.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258537.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258538.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258470.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup

bam=SRR1258471.noN.sorted
samtools mpileup -uf $ref ${bam}.bam |bcftools view - > ${bam}.mpileup
