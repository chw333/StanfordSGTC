library(edgeR)
load('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/GRCh38GTF.rda')

mat = read.table('HRSV-GeneCount', header=T)
mat = mat[,c(1,2,13,14)]
group = factor(c(1,1,2,2))
y <- DGEList(counts=mat,group=group)
y <- calcNormFactors(y)
y <- estimateCommonDisp(y)
y <- estimateTagwiseDisp(y)
et <- exactTest(y)
res = topTags(et,n=70000)
res= as.data.frame(res)
res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res.sig = res[which(res$FDR<0.05),]
res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]

write.table( res, file="deRSV.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="deRSV_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig.proteincoding, file="deRSV_sig_proteincoding.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
