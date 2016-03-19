ref=/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh37.75.dna.fasta
bam=S635A.bam
out=S635A.ase
bam-readcount -f $ref -l S635A.bed $bam -w 0 >$out

bam=CP1.bam
out=CP1.ase
bam-readcount -f $ref -l S635A.bed $bam -w 0 >$out

bam=CP2.bam
out=CP2.ase
bam-readcount -f $ref -l S635A.bed $bam -w 0 >$out
