mat = read.table('Single-Trait-lm-Sig-Sorted')
p = mat[,3]
q = p.adjust(p)
head(q)
