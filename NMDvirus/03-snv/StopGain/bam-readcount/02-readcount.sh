bam=Mock-rep1.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
bam=Mock-rep2.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
bam=RSV_M0.1-rep1.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
bam=RSV_M0.1-rep2.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
bam=RSV_M3-rep1.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
bam=RSV_M3-rep2.bam
bam-readcount -f /mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa -l RSV2-Stopgain-SNV.bed $bam -w 0 >${bam}.Count
