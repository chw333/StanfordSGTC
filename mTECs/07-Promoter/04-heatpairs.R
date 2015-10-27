library(LSD)

mat = read.table('mTECs-Sample-LibrarySize')
LibSize =  mat[,3]
mat = read.table('Mouse_Gene_Promoter_Cov', header=T)
mat = as.matrix(mat[,5:ncol(mat)])
mat.norm = t(t(mat)/LibSize)

pdf('mTECs-Promoter-Cor.pdf')
heatpairs(mat.norm)
dev.off()

pdf('mTECs-Promoter-Cor-log2.pdf')
heatpairs(mat.norm)
dev.off()


