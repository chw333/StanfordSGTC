res.mouse.exp = res.mouse[which(res.mouse$baseMean > 20),]
res.mouse.exp = cbind.data.frame(res.mouse.exp, ids[match(rownames(res.mouse.exp), ids$gene_id), c("gene_name","gene_biotype")])
write.table( res.mouse.exp, file="deMouse_exp.txt", quote = FALSE, sep = "\t",  row.names = T, col.names=NA)
savehistory('test.R')
