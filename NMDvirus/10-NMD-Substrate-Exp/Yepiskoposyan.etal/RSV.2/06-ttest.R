mat = read.table('UPF1SMG6SMG7-KnockDown-UP-Yepiskoposyan.etal2.exp',header=T)
#wh = !(mat[,2]==0 | mat[,3]==0)
wh = mat[,2]>20 & mat[,3]>20
mat = mat[wh,]
t.test(log2(mat[,2]), log2(mat[,3]), paired=T)
