library(DESeq2)
geneCounts = read.table('RSVdelNS-GeneCount2', header=T)
sampleAnnot = read.table('SampleAnnot.txt', header=T)
sampleAnnot$Condition = relevel(sampleAnnot$Condition, 'Mock')

wh = grepl('Mock|delNS_M3',sampleAnnot$Condition)
sampleAnnot = droplevels(sampleAnnot[wh,])
geneCounts = geneCounts[,wh]

dds = DESeqDataSetFromMatrix(geneCounts, sampleAnnot, design=~Condition)
dds = DESeq(dds)
res = results(dds)

load('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/GRCh38GTF.rda')
res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res = res[order(res$padj), ]
res.sig = res[which(res$padj<0.05 & res$baseMean > 10),]
res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]
res.sig.proteincoding.up = res.sig.proteincoding[res.sig.proteincoding$log2FoldChange>=0,]
res.sig.proteincoding.down = res.sig.proteincoding[res.sig.proteincoding$log2FoldChange<0,]
res.sig.nonproteincoding = res.sig[res.sig$gene_biotype != "protein_coding",]

rld = rlog(dds, blind=FALSE)
save(dds, rld, res, res.sig, res.sig.proteincoding, sampleAnnot, file='resDelNS_M3.rda')

write.table( res, file="deDelNS_M3.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="deDelNS_M3_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file="deDelNS_M3_sig_proteincoding.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding.up, file="deDelNS_M3_sig_proteincoding_up.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding.down, file="deDelNS_M3_sig_proteincoding_down.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.nonproteincoding, file="deDelNS_M3_sig_nonproteincoding.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)

geneCounts.norm = counts(dds, normalized=T)
colnames(geneCounts.norm) = colnames(geneCounts)
cn = cbind.data.frame(ids[match(rownames(geneCounts.norm), ids$gene_id), c("gene_name")],geneCounts.norm)
colnames(cn)[1]='gene_symbol'
write.table(cn, file="geneCounts-DelNS_M3-Normalized.txt",quote=F,sep="\t",row.names=T,col.names=NA)

geneCounts.raw = counts(dds, normalized=F)
colnames(geneCounts.raw) = colnames(geneCounts)
cn = cbind.data.frame(ids[match(rownames(geneCounts.raw), ids$gene_id), c("gene_name")],geneCounts.raw)
colnames(cn)[1]='gene_symbol'
write.table(cn, file="geneCounts-DelNS_M3-raw.txt",quote=F,sep="\t",row.names=T,col.names=NA)
