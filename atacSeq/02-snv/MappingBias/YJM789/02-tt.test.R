mat = read.table('5a.flt.bias')
wh = mat[,2] >=5 & mat[,3] >=5
mat = mat[wh,]
t.test(log2(mat[,2]), log2(mat[,3]), paired=T)
summary(mat[,2])
summary(mat[,3])


mat = read.table('5b.flt.bias')
wh = mat[,2] >=5 & mat[,3] >=5
mat = mat[wh,]
t.test(log2(mat[,2]), log2(mat[,3]), paired=T)

summary(mat[,2])
summary(mat[,3])


