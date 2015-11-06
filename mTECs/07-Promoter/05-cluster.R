df = read.table('Mouse_Gene_Promoter_Cov_Norm_Flt', header=T)

mat = log2(df)
mat = t(mat)
d <- dist(mat, method = "euclidean")
fit <- hclust(d, method="ward.D")
groups <- cutree(fit, k=2)
pdf('Mouse_Gene_Promoter_Cov_Norm_Flt_log2.pdf')
p=plot(fit, xlab='', main='Cluster based on promoter coverage')
rect.hclust(fit, k=2, border="red")
dev.off()


mat = t(df)
d <- dist(mat, method = "euclidean")
fit <- hclust(d, method="ward.D")
groups <- cutree(fit, k=2)
pdf('Mouse_Gene_Promoter_Cov_Norm_Flt.pdf')
p=plot(fit, xlab='', main='Cluster based on promoter coverage')
rect.hclust(fit, k=2, border="red")
dev.off()

