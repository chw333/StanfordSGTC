load('resWNV.rda')
fitted.common.scale = t(t(assays(dds)[["mu"]])/sizeFactors(dds))
resduals = counts(dds, normalized=TRUE) - fitted.common.scale

i =1 
pdf(paste0('Residual-Sample-',i,'.pdf'))
plot(log2(fitted.common.scale[,i]), resduals[,i], ylim=c(-1000,1000))
dev.off()

i = 4
pdf(paste0('Residual-Sample-',i,'.pdf'))
plot(log2(fitted.common.scale[,i]), resduals[,i], ylim=c(-1000,1000))
dev.off()
