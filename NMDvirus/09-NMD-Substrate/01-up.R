upf1 = read.table('UPF1-KnockDown-UP', header=T)
smg6 = read.table('SMG6-KnockDown-UP', header=T)
smg7 = read.table('SMG7-KnockDown-UP', header=T)
upf1.gene = upf1[,6]
smg6.gene = smg6[,6]
smg7.gene = smg7[,6]
two = intersect(upf1.gene, smg6.gene)
three = intersect(smg7.gene,two)
write.table(three,row.names=F, col.names=F,sep = '\t',quote=F,file = 'test')
