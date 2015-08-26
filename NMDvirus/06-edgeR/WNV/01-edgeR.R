library(edgeR)
load('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/GRCh38GTF.rda')

mat = read.table('WNV-GeneCount', header=T)
group = factor(rep(c(1,2),time=10))
y <- DGEList(counts=mat,group=group)
y <- calcNormFactors(y)
y <- estimateCommonDisp(y)
y <- estimateTagwiseDisp(y)
et <- exactTest(y)
res = topTags(et,n=20000)
res= as.data.frame(res)
res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res.sig = res[which(res$FDR<0.05),]
res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]

write.table( res, file="deWNV.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="deWNV_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file="deWNV_sig_proteincoding.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
