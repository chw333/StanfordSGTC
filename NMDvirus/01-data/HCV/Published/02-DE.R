load('resDE.rda')
wt.mock = mat[mat$WT.Mock.72FDR<0.05,]
m15.mock = mat[mat$m15.Mock.96FDR<0.05,]
wt.mock = wt.mock[order(wt.mock$WT.Mock.72FDR),]
m15.mock = m15.mock[order(m15.mock$m15.Mock.96FDR),]
write.table(wt.mock,file= 'de_WTvirus-Mock',row.names=F,col.names=T,sep='\t',quote=F)
write.table(m15.mock,file= 'de_m15-Mock',row.names=F,col.names=T,sep='\t',quote=F)
