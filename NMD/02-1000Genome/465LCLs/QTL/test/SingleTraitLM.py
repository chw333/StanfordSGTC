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

SIG = 0.05

def SingleTraitLM(inF1, inF2, ouF):

    geno_reader = gr.genotype_reader_tables(inF1)
    pheno_reader = phr.pheno_reader_tables(inF2)
    dataset = data.QTLData(geno_reader=geno_reader,pheno_reader=pheno_reader)
    geno = dataset.getGenotypes()
    position = dataset.getPos()
    pos,chromBounds = data_util.estCumPosSorted(position=position,offset=0)

    ouFile = open(ouF, 'w')

    P_max = len(dataset.phenotype_ID)
    phenotype_ID = dataset.phenotype_ID[0:P_max]


    for p_ID in phenotype_ID[0:]:
        if p_ID == 'snp_17_59667953':
        #phenotype_vals, sample_idx = dataset.getPhenotypes([pI], center=False)
            phenotype_vals, sample_idx = dataset.getPhenotypes([p_ID])
            phenotype_vals_ranks = preprocess.rankStandardizeNormal(phenotype_vals.values)
            lm_ranks = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals_ranks)
            #pvalues_lm_ranks = pd.DataFrame(data=lm_ranks.pvalues.T,index=dataset.geno_ID,columns=[p_ID])
            pvt = lm_ranks.pvalues.T
            for i in xrange(pvt.shape[0]):
                p = pvt[i,0]
                if p < SIG:
                    ouFile.write('\t'.join([position['chrom'][i], str(position['pos'][i]), str(p), p_ID]) + '\n')
    ouFile.close()


def manhattonPlot(phenotype_ID, pvalues_lm, ouFprefix, pos, chromBounds):
    for ip, p_ID in enumerate(phenotype_ID):
        pl.figure(figsize=[12,4])
        plot_manhattan(posCum=pos['pos_cum'],pv=pvalues_lm[p_ID].values,chromBounds=chromBounds,thr_plotting=0.05)
        pl.title(p_ID)
        pl.savefig(ouFprefix + '.' + p_ID + '.pdf')
        pl.close('all')


def SingleTraitLM_ManhattonPlot(inF1, inF2, SigPhe):

    geno_reader = gr.genotype_reader_tables(inF1)
    pheno_reader = phr.pheno_reader_tables(inF2)
    dataset = data.QTLData(geno_reader=geno_reader,pheno_reader=pheno_reader)
    geno = dataset.getGenotypes()
    position = dataset.getPos()
    pos,chromBounds = data_util.estCumPosSorted(position=position,offset=0)


    P_max = len(dataset.phenotype_ID)
    phenotype_ID = dataset.phenotype_ID[0:P_max]


    for p_ID in phenotype_ID[0:]:
        if p_ID == SigPhe:
            phenotype_vals, sample_idx = dataset.getPhenotypes([p_ID])
            phenotype_vals_ranks = preprocess.rankStandardizeNormal(phenotype_vals.values)
            lm_ranks = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals_ranks)
            pvalues_lm_ranks = pd.DataFrame(data=lm_ranks.pvalues.T,index=dataset.geno_ID,columns=[p_ID])
            manhattonPlot([p_ID], pvalues_lm_ranks, 'NMD-QTL-ManhattonPlot', pos, chromBounds)

#SingleTraitLM_ManhattonPlot('1000Genome-462LCLs-Genotype.hdf5','1000Genome-462LCLs-Phenotype.hdf5','snp_6_31124849')

SingleTraitLM('1000Genome-462LCLs-Genotype.hdf5','1000Genome-462LCLs-Phenotype.hdf5','Single-Trait-lm-Sig')

