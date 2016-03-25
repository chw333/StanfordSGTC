library(DESeq2)
geneCounts = read.table('DCM-GeneCountSymbol', header=T)
Counts = geneCounts[1:nrow(geneCounts),3:ncol(geneCounts)] 
rownames(Counts) = geneCounts[1:nrow(geneCounts),2]

sampleAnnot = read.table('DCM-SampleAnnot', header=T, sep='\t')


#Counts = Counts[1:nrow(Counts), (ncol(Counts)-2):ncol(Counts)]
#sampleAnnot = sampleAnnot[(nrow(sampleAnnot)-2):nrow(sampleAnnot),]

dds = DESeqDataSetFromMatrix(Counts, sampleAnnot, design=~Individual)
dds = DESeq(dds)

Counts.norm = counts(dds, normalized=T)
colnames(Counts.norm) = colnames(Counts)
Count.norm=cbind(geneCounts$GeneName,as.data.frame(Counts.norm))
colnames(Count.norm)[1] = 'GeneName'
write.table(Count.norm, file="DCM-GeneCountSymbol-Normalized",quote=F,sep="\t",row.names=T,col.names=NA)
