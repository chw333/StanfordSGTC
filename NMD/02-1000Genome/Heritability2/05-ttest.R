mat = read.table('G462-Sample-Stopgain-ASE-Escape-Filtered-Ratio')
v1 = mat[mat[,2]==T,3]
v2 = mat[mat[,2]==F,3]
median(v1)
median(v2)
t.test(v1,v2)

mat = read.table('G462-Sample-Stopgain-ASE-Escape-Filtered2-Ratio')
v1 = mat[mat[,2]==T,3]
v2 = mat[mat[,2]==F,3]
median(v1)
median(v2)
t.test(v1,v2)
