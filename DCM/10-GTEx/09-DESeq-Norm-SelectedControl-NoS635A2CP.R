library(DESeq2)
geneCounts = read.table('GTEx_Heart_S635A_TwoCtrl_exp', header=T)
Counts = geneCounts[1:nrow(geneCounts),3:ncol(geneCounts)] 
rownames(Counts) = geneCounts[1:nrow(geneCounts),1]

sampleAnnot = read.table('GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads_heart_sample_S635A_TwoCtrl', header=T, sep='\t')


### random sample
### Heart - Atrial Appendage:    34, 69, 174
### Heart - Left Ventricle:    216, 285, 382
### selected sample
### 192, 70, 134, Atrial Appendage, actual death
### 360, 281, 201, Left Ventricle, actual death
### 179, 142, 125, Atrial Appendage, presumed death
### 336, 312, 350, Left Ventricle, presumed death
sel = c(192, 70, 134, 360, 281, 201, 179, 142, 125, 336, 312, 350)
Counts = Counts[1:nrow(Counts), sel]
sampleAnnot = sampleAnnot[sel,]

sampleAnnot$Tissue=c('Atrial Appendage Actual Death','Atrial Appendage Actual Death','Atrial Appendage Actual Death','Left Ventricle Actual Death','Left Ventricle Actual Death','Left Ventricle Actual Death','Atrial Appendage Presumed Death', 'Atrial Appendage Presumed Death','Atrial Appendage Presumed Death','Left Ventricle Presumed Death', 'Left Ventricle Presumed Death', 'Left Ventricle Presumed Death')

dds = DESeqDataSetFromMatrix(Counts, sampleAnnot, design=~Individual)
dds = DESeq(dds)

Counts.norm = counts(dds, normalized=T)
colnames(Counts.norm) = colnames(Counts)
Count.norm=cbind(geneCounts$Description,as.data.frame(Counts.norm))
colnames(Count.norm)[1] = 'GeneName'
write.table(Count.norm, file="GTEx_Heart_S635A_TwoCtrl_exp-Normalized_RandomControl_NoS635A2CP.txt",quote=F,sep="\t",row.names=T,col.names=NA)

rlg = rlog(dds)
rlg = assay(rlg)
colnames(rlg) = colnames(Counts)
rlg=cbind(geneCounts$Description,as.data.frame(rlg))
colnames(rlg)[1] = 'GeneName'
write.table(rlg, file="GTEx_Heart_S635A_TwoCtrl_exp-rlog_SelectedControl_NoS635A2CP.txt",quote=F,sep="\t",row.names=T,col.names=NA)
