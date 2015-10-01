library(edgeR)
mat = read.table('5a5b-Allele-Masked-Count', header=T)
group = factor(c(1,2,1,2))
y <- DGEList(counts=mat,group=group)
y <- calcNormFactors(y)
y <- estimateCommonDisp(y)
y <- estimateTagwiseDisp(y)
et <- exactTest(y)
res = topTags(et,n=70000)
res= as.data.frame(res)
#res = cbind.data.frame(res, ids[match(rownames(res), ids$gene_id), c("gene_name","gene_biotype")])
res.sig = res[which(res$FDR<0.05),]
#res.sig.proteincoding = res.sig[res.sig$gene_biotype == "protein_coding",]

write.table( res, file="de.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
write.table( res.sig, file="de_sig.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
