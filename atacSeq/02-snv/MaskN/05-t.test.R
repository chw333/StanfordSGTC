mat = read.table('5a5b-Allele-Count', header=T)

mat2 = mat[mat[,5]>=1 & mat[,6]>=1,]
mat3 = mat[mat[,7]>=1 & mat[,8]>=1,]
t.test(log2(mat2[,5]), log2(mat2[,6]))
t.test(log2(mat3[,7]), log2(mat3[,8]))

summary(mat2[,5])
summary(mat2[,6])

summary(mat3[,7])
summary(mat3[,8])



mat2 = mat[mat[,9]>=1 & mat[,10]>=1,]
mat3 = mat[mat[,11]>=1 & mat[,12]>=1,]
t.test(log2(mat2[,9]), log2(mat2[,10]))
t.test(log2(mat3[,11]), log2(mat3[,12]))

summary(mat2[,9])
summary(mat2[,10])

summary(mat3[,11])
summary(mat3[,12])
