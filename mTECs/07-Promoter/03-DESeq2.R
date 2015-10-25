library(DESeq2)

geneCounts = read.table('Mouse_Gene_Promoter_Cov', header=T)
sampleAnnot = read.table('SampleAnnot',head=T)
wh = c(1,2,5,6)
sampleAnnot$Sample = droplevels(sampleAnnot$Sample[wh])
sampleAnnot$Condition = factor(c('high','high','low','low'), levels=c('low','high'))
rownames(sampleAnnot) = sampleAnnot$Sample

geneCounts = geneCounts[,wh + 5]
#geneCountsFlt=geneCounts[rowSums(geneCounts > 20) > ncol(geneCounts)/2,]


dds = DESeqDataSetFromMatrix(geneCounts, sampleAnnot, design=~Condition) #to compare CP2 and CP3 to CP1, unable to use family/gender difference, same comparison here
dds = DESeq(dds)

load("/g/steinmetz/hsun/Stanford/data/HumanGTF.rda")
res = results(dds)
res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res = res[order(res$padj), ]
res.sig = res[which(res$padj<0.05 & res$baseMean > 20),]
res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]
res.sig.proteincoding.up = res.sig.proteincoding[res.sig.proteincoding$log2FoldChange>=0,]
res.sig.proteincoding.down = res.sig.proteincoding[res.sig.proteincoding$log2FoldChange<0,]
res.sig.nonproteincoding = res.sig[res.sig$gene_biotype != "protein_coding",]

#..#write.table( res, file=file.path(outfolder, "deCP1vCP4.txt"), quote = FALSE, sep = "\t",  row.names = FALSE)
write.table( res, file=file.path(outfolder, "deNGLY1.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file=file.path(outfolder, "deNGLY1_sig.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file=file.path(outfolder, "deNGLY1_sig_proteincoding.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding.up, file=file.path(outfolder, "deNGLY1_sig_proteincoding_up.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding.down, file=file.path(outfolder, "deNGLY1_sig_proteincoding_down.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.nonproteincoding, file=file.path(outfolder, "deNGLY1_sig_nonproteincoding.txt"), quote = FALSE, sep = "\t",  row.names = T, col.names=NA)

rld = rlog(dds, blind=FALSE)
save(dds, rld, res, res.sig,res.sig.proteincoding,res.sig.nonproteincoding,sampleAnnot,file=file.path(outfolder, "resNGLY1.rda"))

pdf(file.path(outfolder, "plot_PCA-deNGLY1.pdf"), width=8, height=6)
print(plotPCA(rld, intgroup=c("individual", "sampleStatus","cellType")))
dev.off()

pdf(file.path(outfolder, "plot_MA-deNGLY1.pdf"), width=8, height=6)
plotMA(results(dds), alpha=0.01)
dev.off()

pdf(file.path(outfolder, "plot_dispEst-deNGLY1.pdf"), width=8, height=6)
plotDispEsts(dds)
dev.off()


geneCounts.norm = counts(dds, normalized=T)
cn = cbind.data.frame(ids[match(rownames(geneCounts.norm), ids$gene_id), c("gene_name")],geneCounts.norm)
colnames(cn)[1]='gene_symbol'
write.table(cn, file="geneCounts-Human-Normalized.txt",quote=F,sep="\t",row.names=T,col.names=NA)
save(geneCounts.norm, file = "geneCounts-Human-Normalized.rda")

geneCounts.norm = counts(dds, normalized=F)
cn = cbind.data.frame(ids[match(rownames(geneCounts.norm), ids$gene_id), c("gene_name")],geneCounts.norm)
colnames(cn)[1]='gene_symbol'
write.table(cn, file="geneCounts-Human-raw.txt",quote=F,sep="\t",row.names=T,col.names=NA)
