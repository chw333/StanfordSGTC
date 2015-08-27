bam=S1-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S1-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S2-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S2-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S3-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S3-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S4-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S4-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S5-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S5-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S6-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S6-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S7-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S7-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S8-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S8-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S9-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S9-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S10-WNV.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf
bam=S10-Mock.bam
samtools mpileup  -v -l DCAF11.bed -f $hg38 $bam |bcftools call -c - >${bam}.vcf


