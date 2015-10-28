library(DESeq2)

geneCounts = read.table('Mouse_Gene_Promoter_Cov', header=T)
rownames(geneCounts) = paste(geneCounts$gene,geneCounts$chr,geneCounts$start,geneCounts$end,sep='_')
sampleAnnot = read.table('SampleAnnot',head=T)
wh = c(1,2,7,8)
sampleAnnot = droplevels(sampleAnnot[wh, ])
sampleAnnot$ConditionTspan8 = relevel(sampleAnnot$ConditionTspan8, 'negative') 
rownames(sampleAnnot) = sampleAnnot$Sample

geneCounts = geneCounts[,wh + 4]
#geneCountsFlt=geneCounts[rowSums(geneCounts > 20) > ncol(geneCounts)/2,]


dds = DESeqDataSetFromMatrix(geneCounts, sampleAnnot, design=~ConditionTspan8) 
dds = DESeq(dds)

res = results(dds)
res = res[order(res$padj), ]

res.sig = res[which(res$padj<0.05 & res$baseMean > 20),]
res.sig.up = res.sig[res.sig$log2FoldChange>=0,]
res.sig.down = res.sig[res.sig$log2FoldChange<0,]
rld = rlog(dds, blind=FALSE)

#..#write.table( res, file=file.path(outfolder, "deCP1vCP4.txt"), quote = FALSE, sep = "\t",  row.names = FALSE)
write.table( res, file="MHCII_low_Tspan8_PositiveNegative.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="MHCII_low_Tspan8_PositiveNegative_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.up, file="MHCII_low_Tspan8_PositiveNegative_sig_up.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.down, file="MHCII_low_Tspan8_PositiveNegative_sig_down.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)

save(dds, rld, res, res.sig,sampleAnnot,file="res_MHCII_low_Tspan8_PositiveNegative.rda")

pdf("plot_PCA-MHCII_low_Tspan8_PositiveNegative.pdf", width=8, height=6)
print(plotPCA(rld, intgroup=c("Sample", "ConditionMHCII")))
dev.off()

pdf("plot_MA-MHCII_low_Tspan8_PositiveNegative.pdf", width=8, height=6)
plotMA(results(dds), alpha=0.01)
dev.off()

pdf("plot_dispEst-MHCII_low_Tspan8_PositiveNegative.pdf", width=8, height=6)
plotDispEsts(dds)
dev.off()


geneCounts.norm = counts(dds, normalized=T)
write.table(geneCounts.norm, file="MHCII_low_Tspan8_PositiveNegative-Counts-Normalized.txt",quote=F,sep="\t",row.names=T,col.names=NA)

geneCounts.norm = counts(dds, normalized=F)
write.table(geneCounts.norm, file="MHCII_low_Tspan8_PositiveNegative-Counts-raw.txt",quote=F,sep="\t",row.names=T,col.names=NA)
