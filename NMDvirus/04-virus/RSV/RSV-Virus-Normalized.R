x = read.table('RSV-Virus')
y = read.table('RSV-SizeFactor')
mat = data.frame(y[,1], y[,2], x[,1])
colnames(mat) = c('Sample','SizeFactor','NumberOfVirusReads')
Normalized = mat[,3]/mat[,2]
mat = cbind(mat,Normalized)
write.table(mat, file='RSV-Virus-Normalized', row.names=F, col.names=T, sep='\t', quote=F)
