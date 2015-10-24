mat = read.table('Tspan8_positive_MHCII_HighLow', header=T)
head(mat)
mat$fold_change
sorted(mat$fold_change)
order(mat$fold_change)
mat =mat[order(mat$fold_change),]
head(mat)
tail(mat)
tail(mat)
write.table(mat, file='mat', quote=F, sep='\t', col.names=T, row.names=F)
savehistory('test.R')
