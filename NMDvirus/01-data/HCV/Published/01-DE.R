library(org.Hs.eg.db)
library(annotate)

mat = read.table('GSE64677_VirusvsMock_RNAseq_CountMatrix.txt', sep='\t', header=T)
eg = as.character(mat[,1])
sym = getSYMBOL(eg, data='org.Hs.eg')
mat = cbind(sym, mat)
save(mat, file='resDE.rda')
