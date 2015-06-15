df = read.table('Single-Trait-lm-Sig')
pv = df[,3]
qv = p.adjust(pv, method='fdr')
df.q = cbind(df[,c(1,2,3)], qv, df[,4])
df.q.s = df.q[order(df.q$qv),]
write.table(file = 'Single-Trait-lm-Sig-fdr-sorted', df.q.s, col.names=F, row.names=F, sep = '\t', quote=F)
