mat = read.table('RSV2-Stopgain-SNV-ReadCount-Filtered')
x = (mat[,4] + mat[,5])/2
y = (mat[,6] + mat[,7])/2
t.test(x,y,paired=T)
