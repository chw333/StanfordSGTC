library(edgeR)
load('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/GRCh38GTF.rda')

mat = read.table('HCV-GeneCount', header=T)
mat = mat[,5:8]
group = factor(rep(c(1,2),each=2))
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

write.table( res, file="deHCV2.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="deHCV2_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file="deHCV2_sig_proteincoding.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
