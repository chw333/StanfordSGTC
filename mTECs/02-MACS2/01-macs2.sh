sample=Tspan8_negative_MHCII_high_rep1
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_negative_MHCII_high_rep2
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_negative_MHCII_low_rep1
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_negative_MHCII_low_rep2
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_positive_MHCII_high_rep1
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_positive_MHCII_high_rep2
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_positive_MHCII_low_rep1
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
sample=Tspan8_positive_MHCII_low_rep2
macs2 callpeak -t ${sample}.bam -f BAM -g mm -n $sample -B -q 0.01
