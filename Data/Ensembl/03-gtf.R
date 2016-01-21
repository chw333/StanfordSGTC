#library(rtracklayer)
#gtf=import.gff('Homo_sapiens.GRCh38.81.gtf', format='gtf')
#ids=mcols(gtf)[c("gene_id","gene_name","gene_biotype")]
#ids=as.data.frame(ids)
#save(gtf,ids,file='GRCh38GTF.rda')


library(rtracklayer)
gtf=import.gff('Homo_sapiens.GRCh37.75.gtf', format='gtf')
ids=mcols(gtf)[c("gene_id","gene_name","gene_biotype")]
ids=as.data.frame(ids)
save(gtf,ids,file='GRCh37GTF.rda')
