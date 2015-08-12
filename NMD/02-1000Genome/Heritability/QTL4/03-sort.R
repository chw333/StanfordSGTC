mat = read.table('Single-Trait-lm-Sig')
head(mat)
mat = mat[order(mat[,3]),]
head(mat)
write.table(mat, file = 'Single-Trait-lm-Sig-Sorted', quote=F, sep='\t', row.names=F, col.names=F)

mat = read.table('Single-Trait-lm-Sig2')
head(mat)
mat = mat[order(mat[,3]),]
head(mat)
write.table(mat, file = 'Single-Trait-lm-Sig2-Sorted', quote=F, sep='\t', row.names=F, col.names=F)
