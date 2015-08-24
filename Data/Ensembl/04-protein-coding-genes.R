load('GRCh38GTF.rda')
ids.pro=ids[ids$gene_biotype=='protein_coding',]
ids.pro.uni=unique(ids.pro[,2])
ids.pro.uni = ids.pro.uni[!grepl('[.-]', ids.pro.uni)]
mat = data.frame(gene=ids.pro.uni)
write.table(mat,file='GRCh38-ProteinCoding-Genes',quote=F,sep='\t',col.names=F,row.names=F)
