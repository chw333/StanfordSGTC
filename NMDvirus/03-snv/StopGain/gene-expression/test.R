#mat = read.table('geneCounts-RSV_M3-Normalized.checkGene')
mat = read.table('geneCounts-RSV_M3-Normalized.checkGene-mc')
x = (mat[,3] + mat[,4])/2
y = (mat[,5] + mat[,6])/2
t.test(x,y, paired=T)
t.test(log2(x),log2(y), paired=T)
