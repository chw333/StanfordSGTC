library(LSD)

mat = read.table('mTECs-Sample-LibrarySize')
LibSize =  mat[,3]
mat = read.table('Mouse_Gene_Promoter_Cov', header=T)
mat2 = as.matrix(mat[,5:ncol(mat)])
###mat.norm = t(t(mat2)/LibSize)
mat.norm=mat2

pdf('mTECs-Promoter-Cor.pdf')
heatpairs(mat.norm)
dev.off()


wh = apply(mat.norm, 1, function(x){any(x < 5)})
##wh = apply(mat.norm, 1, function(x){any(x == 0)})
mat.norm.flt = mat.norm[!wh,]

pdf('mTECs-Promoter-Cor-log2.pdf')
heatpairs(log2(mat.norm.flt))
dev.off()



write.table(mat.norm.flt, file='Mouse_Gene_Promoter_Cov_Norm_Flt',row.names=F, col.names=T, quote=F, sep='\t')


