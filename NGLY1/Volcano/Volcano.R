library(calibrate)
df = read.table('deNGLY1.txt', header=T)
res = subset(df, (padj<0.05 & gene_biotype=='protein_coding') | gene_name=='NGLY1')

svg('Volcano.svg')
with(res, plot(log2FoldChange, -log10(padj), pch=20, main="Significantly differentially expressed genes (padj < 0.05)", xlim=c(-2,2)))
with(subset(res, gene_name=='NGLY1'), points(log2FoldChange, -log10(padj), pch=20, col="red"))
with(subset(res, gene_name %in% c('PSMB1','PSMC2','PSMD1','PSMD11','PSMD14')), points(log2FoldChange, -log10(padj), pch=20, col="blue"))
lim=par('usr')
lines(c(lim[1], lim[2]),c(-log10(0.05), -log10(0.05)), lty=2)

with(subset(res, gene_name=='PSMD1'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))
with(subset(res, gene_name=='PSMD11'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))
with(subset(res, gene_name=='PSMD14'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))
with(subset(res, gene_name=='PSMB1'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))
with(subset(res, gene_name=='PSMC2'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))
with(subset(res, gene_name=='NGLY1'), textxy(log2FoldChange, -log10(padj), labs=gene_name, cex=.8))

dev.off()

