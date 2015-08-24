samtools view -b SRR497699/accepted_hits.bam -q 30 -@ 8 -o HIV_12-rep1.bam
samtools index HIV_12-rep1.bam
samtools view -b SRR497700/accepted_hits.bam -q 30 -@ 8 -o HIV_12-rep2.bam
samtools index HIV_12-rep2.bam
samtools view -b SRR497701/accepted_hits.bam -q 30 -@ 8 -o HIV_12-rep3.bam
samtools index HIV_12-rep3.bam
samtools view -b SRR497702/accepted_hits.bam -q 30 -@ 8 -o HIV_24-rep1.bam
samtools index HIV_24-rep1.bam
samtools view -b SRR497703/accepted_hits.bam -q 30 -@ 8 -o HIV_24-rep2.bam
samtools index HIV_24-rep2.bam
samtools view -b SRR497704/accepted_hits.bam -q 30 -@ 8 -o HIV_24-rep3.bam
samtools index HIV_24-rep3.bam
samtools view -b SRR497705/accepted_hits.bam -q 30 -@ 8 -o Mock_12-rep1.bam
samtools index Mock_12-rep1.bam
samtools view -b SRR497706/accepted_hits.bam -q 30 -@ 8 -o Mock_12-rep2.bam
samtools index Mock_12-rep2.bam
samtools view -b SRR497707/accepted_hits.bam -q 30 -@ 8 -o Mock_12-rep3.bam
samtools index Mock_12-rep3.bam
samtools view -b SRR497708/accepted_hits.bam -q 30 -@ 8 -o Mock_24-rep1.bam
samtools index Mock_24-rep1.bam
samtools view -b SRR497709/accepted_hits.bam -q 30 -@ 8 -o Mock_24-rep2.bam
samtools index Mock_24-rep2.bam
