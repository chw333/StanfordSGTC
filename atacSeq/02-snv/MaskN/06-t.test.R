mat = read.table('5a-Allele-Count')
mat2 = mat[mat[,5]>=1 & mat[,6]>=1,]
mat3 = mat[mat[,7]>=1 & mat[,8]>=1,]
t.test(log2(mat2[,5]), log2(mat2[,6]))
t.test(log2(mat2[,5]), log2(mat2[,6]),paired=T)
t.test(log2(mat3[,7]), log2(mat3[,8]))
t.test(log2(mat3[,7]), log2(mat3[,8]),paired=T)

summary(mat2[,5])
summary(mat2[,6])

summary(mat3[,7])
summary(mat3[,8])
