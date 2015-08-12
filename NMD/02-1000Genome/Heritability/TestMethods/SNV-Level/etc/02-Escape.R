mat = read.table('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Escape')
v1 = mat[mat[,1]=='unEscaped',2]
v2 = mat[mat[,1]=='Escaped',2]
median(v1)
median(v2)
t.test(v1,v2)
