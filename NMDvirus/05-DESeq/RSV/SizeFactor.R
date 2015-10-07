library(DESeq2)
geneCounts = read.table('HRSV-GeneCount', header=T)
sampleAnnot = read.table('SampleAnnot.txt', header=T)
sampleAnnot$Condition = relevel(sampleAnnot$Condition, 'HRSV0h')
dds = DESeqDataSetFromMatrix(geneCounts, sampleAnnot, design=~Condition)
x=estimateSizeFactors(dds)
sf = x$sizeFactor
sf=data.frame(sf)
rownames(sf) = sampleAnnot$Sample
write.table(sf, file='RSV-SizeFactor', row.names=T, col.names=F, quote=F, sep='\t')
