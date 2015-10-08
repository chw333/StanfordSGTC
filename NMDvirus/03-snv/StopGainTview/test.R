mat = read.table('RSV2_M3-Stopgain-SNV-gene-formated-exp-mc')
t.test(mat[,9], mat[,10], paired=T)


mat = read.table('RSV2_M0.1-Stopgain-SNV-gene-formated-exp-mc')
t.test(mat[,9], mat[,10], paired=T)

mat = read.table('RSV-Stopgain-SNV-gene-formated-exp-mc')
t.test(mat[,9], mat[,10], paired=T)
