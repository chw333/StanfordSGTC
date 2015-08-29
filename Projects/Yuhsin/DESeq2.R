library(DESeq2)
load('MouseGTF.rda')

mat = read.table('readsPerGenes.txt',header=T)
sample = colnames(mat)
condition = rep(c('control','infected'), times=c(28, 48))
sampleAnnot = data.frame(sample, condition)

dds = DESeqDataSetFromMatrix(mat, sampleAnnot, design=~condition)
dds = DESeq(dds)
res = results(dds)
res = res[order(res$padj), ]

res.mouse = res[grepl('ENSMUSG',rownames(res)),]
res.other = res[!grepl('ENSMUSG',rownames(res)),]

res.mouse.sig = res.mouse[which(res.mouse$padj<0.05 & res.mouse$baseMean > 20),]
res.mouse.sig = cbind.data.frame(res.mouse.sig, ids[match(rownames(res.mouse.sig), ids$gene_id), c("gene_name","gene_biotype")])

res.other.sig = res.other[which(res.other$padj<0.05 & res.other$baseMean > 20),]

write.table( res.mouse.sig, file="deMouse_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.other.sig, file="deOther_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)


#geneCounts.norm = counts(dds, normalized=T)
#write.table(geneCounts.norm, file="geneCounts-Mouse-Normalized.txt",quote=F,sep="\t",row.names=T,col.names=NA)

#res.mouse.exp = res.mouse[which(res.mouse$baseMean > 20),]
#res.mouse.exp = cbind.data.frame(res.mouse.exp, ids[match(rownames(res.mouse.exp), ids$gene_id), c("gene_name","gene_biotype")])
#write.table( res.mouse.exp, file="deMouse_exp.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
