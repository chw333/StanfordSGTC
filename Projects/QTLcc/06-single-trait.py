import matplotlib
matplotlib.use('Agg')
import limix.io.genotype_reader as gr
import limix.io.phenotype_reader as phr
import limix.io.data as data
import scipy as sp
import pylab as pl
import pandas as pd
import limix.io.data_util as data_util
from limix.utils.plot import *
import limix.utils.preprocess as preprocess
import limix.modules.qtl as qtl
import limix.stats.fdr as fdr


geno_reader = gr.genotype_reader_tables('Yeast-Genotype.hdf5')
pheno_reader = phr.pheno_reader_tables('Yeast-Phenotype.hdf5')
dataset = data.QTLData(geno_reader=geno_reader,pheno_reader=pheno_reader)
geno = dataset.getGenotypes()
position = dataset.getPos()
pos,chromBounds = data_util.estCumPos(position=position,offset=0)
P_max = len(dataset.phenotype_ID)
phenotype_ID = dataset.phenotype_ID[0:P_max]
phenotype_vals, sample_idx = dataset.getPhenotypes(phenotype_ID)
N = geno.shape[0]
S = geno.shape[1]
P = phenotype_vals.shape[1]

SIG = 0.0000001
def significant(pvalues_lm,ouF):
    SigPhe = set()
    ouFile = open(ouF,'w')
    for i in range(pvalues_lm.shape[1]):
        n = -1
        for x in pvalues_lm.ix[:,i]:
            n += 1
            if x < SIG:
                ouFile.write("%s\t%s_%s\t%s\t%s"%(n,pos['chrom'][n], pos['pos'][n],pvalues_lm.columns[i],x) + '\n')
                SigPhe.add(pvalues_lm.columns[i])
    ouFile.close()
    return SigPhe

def manhattonPlot(phenotype_ID, pvalues_lm, ouFprefix):
    for ip, p_ID in enumerate(phenotype_ID):
        pl.figure(figsize=[12,4])
        plot_manhattan(posCum=pos['pos_cum'],pv=pvalues_lm[p_ID].values,chromBounds=chromBounds,thr_plotting=0.05)
        pl.title(p_ID)
        pl.savefig(ouFprefix + '.' + p_ID + '.pdf')
        pl.close('all')

phenotype_vals_ranks = preprocess.rankStandardizeNormal(phenotype_vals.values)
lm_ranks = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals_ranks)
pvalues_lm_ranks = pd.DataFrame(data=lm_ranks.pvalues.T,index=dataset.geno_ID,columns=phenotype_ID)
SigPhe = significant(pvalues_lm_ranks,'QTL-lm-significant-rank')
manhattonPlot(SigPhe, pvalues_lm_ranks, 'QTL-lm-significant-rank')

