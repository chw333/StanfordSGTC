mat = read.table('Single-Trait-lm-Sig2-Gene')
mat=mat[order(mat[,3]),]
write.table(mat,file='Single-Trait-lm-Sig2-Gene-Sorted',quote=F, row.names=F, col.names=F, sep='\t')


mat = read.table('Single-Trait-lm-Sig-Sorted-Gene')
mat=mat[order(mat[,3]),]
write.table(mat,file='Single-Trait-lm-Sig-Gene-Sorted',quote=F, row.names=F, col.names=F, sep='\t')
