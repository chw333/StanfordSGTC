mat = read.table('5a.dp')
wh = mat[,1]!='chrM'
mat = mat[wh,]
summary(mat[,3])


mat = read.table('5b.dp')
wh = mat[,1]!='chrM'
mat = mat[wh,]
summary(mat[,3])


mat = read.table('S96a.dp')
wh = mat[,1]!='chrM'
mat = mat[wh,]
summary(mat[,3])


mat = read.table('S96b.dp')
wh = mat[,1]!='chrM'
mat = mat[wh,]
summary(mat[,3])
