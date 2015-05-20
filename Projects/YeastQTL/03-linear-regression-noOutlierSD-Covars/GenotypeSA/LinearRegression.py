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
from PHENO import *
import gzip
import os

geno_reader = gr.genotype_reader_tables('../Yeast-Genotype-noMissing-SA.hdf5')
pheno_reader = phr.pheno_reader_tables('../Yeast-Phenotype-noOutlierSD.hdf5')
dataset = data.QTLData(geno_reader=geno_reader,pheno_reader=pheno_reader)
geno = dataset.getGenotypes()
position = dataset.getPos()
pos,chromBounds = data_util.estCumPos(position=position,offset=0)
P_max = len(dataset.phenotype_ID)
#P_max = 6
phenotype_ID = dataset.phenotype_ID[0:P_max:2]
phenotype_vals, sample_idx = dataset.getPhenotypes(phenotype_ID)
N = geno.shape[0]
S = geno.shape[1]
P = phenotype_vals.shape[1]


phenotype_vals_boxcox, maxlog = preprocess.boxcox(phenotype_vals.values)
phenotype_vals_ranks = preprocess.rankStandardizeNormal(phenotype_vals.values)

#### comment ALL, for saving time
SIG = 0.000001
def significant(pvalues_lm,ouF):
    SigPhe = set()
    ALL = []
    ouFile = open(ouF,'w')
    ouFile2 = open(ouF+'-ALL','w')
    for i in range(pvalues_lm.shape[1]):
        n = -1
        for x in pvalues_lm.ix[:,i]:
            n += 1
            ALL.append([n, pos['chrom'][n], pos['pos'][n], i*2, pvalues_lm.columns[i], x])
            if x < SIG:
                ouFile.write("%s\t%s_%s\t%s\t%s\t%s"%(n,pos['chrom'][n], pos['pos'][n],i*2,pvalues_lm.columns[i],x) + '\n')
                SigPhe.add(pvalues_lm.columns[i])
    ouFile.close()
    ALL.sort(cmp = lambda x,y:cmp(x[-1],y[-1]))
    for x in ALL:
        ouFile2.write("%s\t%s_%s\t%s\t%s\t%s"%(x[0],x[1],x[2],x[3],x[4],x[5]) + '\n')
    ouFile2.close()
    return SigPhe


def Permutation(N,ouFprefix):
    #for n in range(N):
    for n in range(N):
        ouF = ouFprefix + '-' + str(n)
        ouFile = open(ouF, 'w')
        #perm = np.random.permutation(phenotype_vals.values)
        perm = []
        for i in range(len(phenotype_vals.values[0])):
            p = np.random.permutation(phenotype_vals.values[:,i])
            perm.append(p)
        perm = np.array(perm)
        perm = perm.T

        lm = qtl.test_lm(snps=geno[sample_idx],pheno=perm, covs=covars_conditional)
        pvalues_lm = pd.DataFrame(data=lm.pvalues.T,index=dataset.geno_ID,columns=phenotype_ID)
        ALL = []
        for i in range(pvalues_lm.shape[1]):
            n = -1
            for x in pvalues_lm.ix[:,i]:
                n += 1
                #ALL.append([n, pos['chrom'][n], pos['pos'][n], i*2, pvalues_lm.columns[i], x]) 
                ouFile.write("%s_%s\t%s\t%.4f"%(pos['chrom'][n],pos['pos'][n],NAME.index(pvalues_lm.columns[i]),x) + '\n')
        #for x in ALL:
        ouFile.close()
        zip_in = open(ouF, 'rb')
        zip_out = gzip.open(ouF+'.gz', 'wb')
        zip_out.writelines(zip_in)
        zip_in.close()
        zip_out.close()
        os.remove(ouF)



chs = ['II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']
def manhattonPlot(phenotype_ID, pvalues_lm, ouFprefix):
    for ip, p_ID in enumerate(phenotype_ID):
        pl.figure(figsize=[12,4])
        #plot_manhattan(posCum=pos['pos_cum'],pv=pvalues_lm[p_ID].values,chromBounds=chromBounds,thr_plotting=0.05)
        plot_manhattan(posCum=pos['pos_cum'],pv=pvalues_lm[p_ID].values,chromBounds=chromBounds,thr_plotting=0.05, xticklabelsList=chs)
        pl.title('%s, SA'%p_ID.split('-mean')[0])
        pl.savefig(ouFprefix + '.' + p_ID + '.pdf')
        pl.close('all')

imax = 3137
### II:476596
covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((phenotype_vals.values.shape[0],1))),1)

Permutation(1000, 'Permutation/QTL-lm-untransformed')

###lm = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals.values, covs=covars_conditional)
###pvalues_lm = pd.DataFrame(data=lm.pvalues.T,index=dataset.geno_ID,columns=phenotype_ID)
###SigPhe = significant(pvalues_lm, 'QTL-lm-significant-untransformed')
###manhattonPlot(SigPhe, pvalues_lm, 'QTL-lm-significant-untransformed')
###
###
###lm_boxcox = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals_boxcox, covs=covars_conditional)
###pvalues_lm_boxcox = pd.DataFrame(data=lm_boxcox.pvalues.T,index=dataset.geno_ID,columns=phenotype_ID)
###SigPhe = significant(pvalues_lm_boxcox, 'QTL-lm-significant-boxcox')
###manhattonPlot(SigPhe, pvalues_lm_boxcox, 'QTL-lm-significant-boxcox')
###
###
###lm_ranks = qtl.test_lm(snps=geno[sample_idx],pheno=phenotype_vals_ranks, covs=covars_conditional)
###pvalues_lm_ranks = pd.DataFrame(data=lm_ranks.pvalues.T,index=dataset.geno_ID,columns=phenotype_ID)
###SigPhe = significant(pvalues_lm_ranks,'QTL-lm-significant-rank')
###manhattonPlot(SigPhe, pvalues_lm_ranks, 'QTL-lm-significant-rank')
###
###def phenoGeno(ouFprefix):
###
###    for ip, p_ID in enumerate(dataset.phenotype_ID[0:P_max:2]):
###        S = set()
###        for n in range(len(lm.pvalues[ip])):
###            if lm.pvalues[ip][n] < SIG:
###                S.add(n)
###        for n in range(len(lm_boxcox.pvalues[ip])):
###            if lm_boxcox.pvalues[ip][n] < SIG:
###                S.add(n)
###        for n in range(len(lm_ranks.pvalues[ip])):
###            if lm_ranks.pvalues[ip][n] < SIG:
###                S.add(n)
###        print(S)
###
###        for n in S:
###            imax = n
###            pl.figure(figsize=[15,5])#create the figure
###            plt = pl.subplot(1,3,1)#the untransformed phenotypes
###            pheno_vals, s_idx = dataset.getPhenotypes([p_ID])
###            pl.plot(geno[s_idx,imax]+0.05*np.random.randn(geno[s_idx,imax].shape[0]),pheno_vals.values,'.',alpha=0.5)
###        
###            pl.title("%s" % p_ID.split('-mean')[0])
###            pl.xlabel('%s:%s, SA'%(pos.ix[n]['chrom'], pos.ix[n]['pos']))
###            pl.ylabel("Phenotype")
###            pl.xlim([-0.5,1.5])
###            
###            plt = pl.subplot(1,3,2)#the Box-Cox transformed phenotypes
###            pl.plot(geno[s_idx,imax]+0.05*np.random.randn(geno[s_idx,imax].shape[0]),phenotype_vals_boxcox[s_idx[sample_idx],ip],'.',alpha=0.5)
###            
###            pl.xlabel('%s:%s, SA'%(pos.ix[n]['chrom'], pos.ix[n]['pos']))
###            pl.ylabel("Phenotype")
###            pl.xlim([-0.5,1.5])
###            #pl.title("%s, boxcox" % p_ID)
###            pl.title("boxcox transformed")
###            
###            plt = pl.subplot(1,3,3)#the rank transformed phenotypes
###            pl.plot(geno[s_idx,imax]+0.05*np.random.randn(geno[s_idx,imax].shape[0]),phenotype_vals_ranks[s_idx[sample_idx],ip],'.',alpha=0.5)
###            
###            #pl.plot([0,1],[pheno_vals.values[i_0].mean(),pheno_vals.values[~i_0].mean()])
###            pl.xlabel('%s:%s, SA'%(pos.ix[n]['chrom'], pos.ix[n]['pos']))
###            pl.ylabel("Phenotype")
###            pl.xlim([-0.5,1.5])
###            #pl.title("%s, ranks" % p_ID)
###            pl.title("ranks transformed")
###    
###            pl.savefig(ouFprefix + '.' + p_ID + '.%s-%s'%(pos.ix[n]['chrom'], pos.ix[n]['pos'])+ '.pdf')
###            pl.close('all')
###    
###phenoGeno('QTL-lm-genotype-phenotype')
