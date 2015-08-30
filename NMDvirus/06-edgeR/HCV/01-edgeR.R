library(edgeR)
load('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/GRCh38GTF.rda')

mat = read.table('HCV-GeneCount', header=T)
mat = mat[,1:4]
group = factor(rep(c(1,2,1,2),each=2))
y <- DGEList(counts=mat,group=group)
y <- calcNormFactors(y)
y <- estimateCommonDisp(y)
y <- estimateTagwiseDisp(y)

individual = factor(rep(1:2, each=4))
design = model.matrix(~individual + group)

y <- estimateGLMCommonDisp(y,design)
y <- estimateGLMTrendedDisp(y,design)
y <- estimateGLMTagwiseDisp(y,design)
fit <- glmFit(y,design)
lrt <- glmLRT(fit)
res = topTags(lrt,n=20000)
res= as.data.frame(res)
res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res.sig = res[which(res$FDR<0.05),]
res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]

write.table( res, file="deHCV_GLM.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="deHCV_sig_GLM.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file="deHCV_sig_proteincoding_GLM.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
