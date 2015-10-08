mat = read.table('RSV2_M3-Stopgain-SNV-gene-exp')
t.test(mat[,2], mat[,3], paired=T)


mat = read.table('RSV2_M0.1-Stopgain-SNV-gene-exp')
t.test(mat[,2], mat[,3], paired=T)

mat = read.table('RSV-Stopgain-SNV-gene-exp')
t.test(mat[,2], mat[,3], paired=T)
