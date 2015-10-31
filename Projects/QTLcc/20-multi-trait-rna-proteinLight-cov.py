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
SIG = 0.0000001
FDR = 0.05


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
sample_relatedness_unnormalized = dataset.getCovariance(normalize=False)
sample_relatedness  = sample_relatedness_unnormalized/ \
    sample_relatedness_unnormalized.diagonal().mean()



def marker():
    D = {}
    inFile = open('Yeast-Mark-Pos')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        mrk = fields[0]
        ch = fields[1]
        start = int(fields[2])
        end = int(fields[3])
        center = int((start + end)/2)
        D[ch+':'+str(center)] = mrk
    inFile.close()
    return D
M = marker()


def Gene(inF1, inF2):
    G2 = []
    G3 = []
    L = []
    inFile = open(inF1)
    for line in inFile:
        line = line.strip()
        L.append(line)
    inFile.close()

    inFile = open(inF2)
    H = inFile.readline().strip().split('\t')
    inFile.close()

    for x in L:
        if x + ':' + 'RNA' in H and x + ':' + 'ProteinLight' in H:
            G2.append(x)
    for x in L:
        if x + ':' + 'RNA' in H and x + ':' + 'ProteinLight' in H and x + ':' + 'ProteinHeavy' in H:
            G3.append(x)

    return [G2, G3]
G = Gene('Yeast-Phenotype-Genes', 'Yeast-Phenotype-Formated')

print(len(G[0]))
print(len(G[1]))
print(set(G[0]) - set(G[1]))

def manhattonPlot(p_ID, pvalues, ouFprefix):
    pl.figure(figsize=[12,4])
    plot_manhattan(posCum=pos['pos_cum'],pv=pvalues[p_ID].values,chromBounds=chromBounds,thr_plotting=0.05)
    pl.title(p_ID)
    pl.savefig(ouFprefix + '.' + p_ID + '.pdf')
    pl.close('all')

def manhattonPlotSpecific(p_ID, pvalues, ouFprefix):
    pl.figure(figsize=[12,4])
    plot_manhattan(posCum=pos['pos_cum'],pv=pvalues['specific'].values,chromBounds=chromBounds,thr_plotting=0.05)
    pl.title(p_ID)
    pl.savefig(ouFprefix + '.' + p_ID + '.pdf')
    pl.close('all')

    pl.figure(figsize=[12,4])
    plot_manhattan(posCum=pos['pos_cum'],pv=pvalues['alternative_any'], chromBounds=chromBounds,colorS='k',colorNS='k',alphaNS=0.05,labelS='any')
    plot_manhattan(posCum=pos['pos_cum'],pv=pvalues['null_common'], chromBounds=chromBounds,colorS='y',colorNS='y',alphaNS=0.05,labelS='common')
    plot_manhattan(posCum=pos['pos_cum'],pv=pvalues['specific'], chromBounds=chromBounds,colorS='r',colorNS='r',alphaNS=0.05,labelS='specific')
    pl.title(p_ID)
    pl.legend(loc='upper right')
    pl.savefig(ouFprefix + '.AnyCommSpec.' + p_ID + '.pdf')
    pl.close('all')




def any_effect(ouF):
    S = []
    ALL = []
    ouFile = open(ouF, 'w')
    ###ouFile2 = open(ouF.split('-Sig')[0] + '-ALL', 'w')
    gs = G[0]
    for gene in gs:
        phenotype_names = [gene + ':RNA', gene + ':ProteinLight']
        phenotype_query = "(phenotype_ID in %s)" %  str(phenotype_names)
        data_subsample = dataset.subsample_phenotypes(phenotype_query=phenotype_query,intersection=True)
        snps = data_subsample.getGenotypes(impute_missing=True)
        phenotypes,sample_idx = data_subsample.getPhenotypes(phenotype_query=phenotype_query, intersection=True)
        sample_relatedness = data_subsample.getCovariance()
        phenotypes_vals_ranks = preprocess.rankStandardizeNormal(phenotypes.values)

        N, P = phenotypes.shape          

        imax = 735
        covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((N,1))),1)

        covs =  None                #covariates
        Acovs = None                #the design matrix for the covariates   
        Asnps = sp.eye(P)           #the design matrix for the SNPs
        K1r = sample_relatedness    #the first sample-sample covariance matrix (non-noise)
        K2r = sp.eye(N)             #the second sample-sample covariance matrix (noise)
        K1c = None                  #the first phenotype-phenotype covariance matrix (non-noise)
        K2c = None                  #the second phenotype-phenotype covariance matrix (noise)
        covar_type = 'freeform'     #the type of the trait/trait covariance to be estimated 
        searchDelta = False         #specify if delta should be optimized for each SNP
        test="lrt"              
        lmm, pv = qtl.test_lmm_kronecker(snps,phenotypes_vals_ranks,covs=covs,Acovs=Acovs, Asnps=Asnps,K1r=K1r,trait_covar_type=covar_type)
        pvalues = pd.DataFrame(data=pv.T,index=data_subsample.geno_ID,columns=[gene])
        qvalues = fdr.qvalues(pv[0])
        flag = 0
        for n in range(pvalues.shape[0]):
            k = position.ix[n]['chrom']+':'+str(position.ix[n]['pos'])
            ###ALL.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene])
            #if pvalues.ix[n][0] < SIG:
            if qvalues[n] < FDR:
                flag = 1
                #ouFile.write('\t'.join([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene]) + '\n')
                S.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]), str(qvalues[n]),gene])
        ####if flag:
        ####    manhattonPlot(gene, pvalues,ouF)
    S.sort(cmp = lambda x,y:cmp(float(x[3]),float(y[3])))
    for item in S:
        ouFile.write('\t'.join(item) + '\n')
    ouFile.close()

    ###ALL.sort(cmp = lambda x,y:cmp(float(x[3]),float(y[3])))
    ###for item in ALL:
    ###    ouFile2.write('\t'.join(item) + '\n')
    ###ouFile2.close()



def common_effect(ouF):
    S = []
    ALL = []
    ouFile = open(ouF, 'w')
    ###ouFile2 = open(ouF.split('-Sig')[0] + '-ALL', 'w')
    gs = G[0]
    for gene in gs:
        phenotype_names = [gene + ':RNA', gene + ':ProteinLight']
        phenotype_query = "(phenotype_ID in %s)" %  str(phenotype_names)
        data_subsample = dataset.subsample_phenotypes(phenotype_query=phenotype_query,intersection=True)
        snps = data_subsample.getGenotypes(impute_missing=True)
        phenotypes,sample_idx = data_subsample.getPhenotypes(phenotype_query=phenotype_query, intersection=True)
        sample_relatedness = data_subsample.getCovariance()
        phenotypes_vals_ranks = preprocess.rankStandardizeNormal(phenotypes.values)

        N, P = phenotypes.shape          

        imax = 735
        ### II:476596
        #covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((phenotypes_vals_ranks.values.shape[0],1))),1)
        covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((N,1))),1)

        covs =  None                #covariates
        Acovs = None                #the design matrix for the covariates   
        #Asnps = sp.eye(P)           #the design matrix for the SNPs
        Asnps = sp.ones((1,P)) 
        K1r = sample_relatedness    #the first sample-sample covariance matrix (non-noise)
        K2r = sp.eye(N)             #the second sample-sample covariance matrix (noise)
        K1c = None                  #the first phenotype-phenotype covariance matrix (non-noise)
        K2c = None                  #the second phenotype-phenotype covariance matrix (noise)
        covar_type = 'freeform'     #the type of the trait/trait covariance to be estimated 
        searchDelta = False         #specify if delta should be optimized for each SNP
        test="lrt"              
        lmm, pv = qtl.test_lmm_kronecker(snps,phenotypes_vals_ranks,covs=covs,Acovs=Acovs, Asnps=Asnps,K1r=K1r,trait_covar_type=covar_type)
        pvalues = pd.DataFrame(data=pv.T,index=data_subsample.geno_ID,columns=[gene])
        flag = 0
        qvalues = fdr.qvalues(pv[0])
        for n in range(pvalues.shape[0]):
            k = position.ix[n]['chrom']+':'+str(position.ix[n]['pos'])
            ###ALL.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene])
            if qvalues[n] < FDR:
                flag = 1
                #print(pvalues)
                #ouFile.write('\t'.join([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene]) + '\n')
                S.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]), str(qvalues[n]),gene])
        ####if flag:
        ####    manhattonPlot(gene, pvalues,ouF)
    S.sort(cmp = lambda x,y:cmp(float(x[4]),float(y[4])))
    for item in S:
        ouFile.write('\t'.join(item) + '\n')

    ###ALL.sort(cmp = lambda x,y:cmp(float(x[3]),float(y[3])))
    ###for item in ALL:
    ###    ouFile2.write('\t'.join(item) + '\n')
    ###ouFile2.close()
    
    ouFile.close()


def specific_effect(ouF):
    S = []
    ALL = []
    ouFile = open(ouF, 'w')
    ouFile.write('\t'.join(['Marker','Chr','Position','Specific_pvalue','Common_pvalue','Any_pvalue','Specific_qvalue','Common_qvalue','Any_qvalue','Gene']) + '\n')
    ###ouFile2 = open(ouF.split('-Sig')[0] + '-ALL', 'w')
    gs = G[0]
    #gs = G[0][80:81]
    for gene in gs:
        phenotype_names = [gene + ':RNA', gene + ':ProteinLight']
        phenotype_query = "(phenotype_ID in %s)" %  str(phenotype_names)
        data_subsample = dataset.subsample_phenotypes(phenotype_query=phenotype_query,intersection=True)
        snps = data_subsample.getGenotypes(impute_missing=True)
        phenotypes,sample_idx = data_subsample.getPhenotypes(phenotype_query=phenotype_query, intersection=True)
        sample_relatedness = data_subsample.getCovariance()
        phenotypes_vals_ranks = preprocess.rankStandardizeNormal(phenotypes.values)

        N, P = phenotypes.shape          

        imax = 735
        ### II:476596
        #covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((phenotypes_vals_ranks.values.shape[0],1))),1)
        covars_conditional=np.concatenate((geno[sample_idx,imax:imax+1],np.ones((N,1))),1)

        covs =  None                #covariates
        Acovs = None                #the design matrix for the covariates   
        Asnps0 = sp.ones((1,P))     #the design matrix for the SNPs
        Asnps1 = sp.zeros((2,P))
        Asnps1[0,:] = 1.0
        Asnps1[1,0] = 1.0
        K1r = sample_relatedness    #the first sample-sample covariance matrix (non-noise)
        K2r = sp.eye(N)             #the second sample-sample covariance matrix (noise)
        K1c = None                  #the first phenotype-phenotype covariance matrix (non-noise)
        K2c = None                  #the second phenotype-phenotype covariance matrix (noise)
        covar_type = 'freeform'     #the type of the trait/trait covariance to be estimated 
        searchDelta = False         #specify if delta should be optimized for each SNP
        test="lrt"              
        #lmm, pv = qtl.test_lmm_kronecker(snps,phenotypes_vals_ranks,covs=covs,Acovs=Acovs, Asnps=Asnps,K1r=K1r,trait_covar_type=covar_type)
        pv = qtl.test_interaction_lmm_kronecker(snps=snps,phenos=phenotypes_vals_ranks, covs=covs,Acovs=Acovs,Asnps1=Asnps1,Asnps0=Asnps0,K1r=K1r,K2r=K2r,K1c=K1c,K2c=K2c,trait_covar_type=covar_type,searchDelta=searchDelta)

        #pvalues = pd.DataFrame(data=pv.T,index=data_subsample.geno_ID,columns=[gene])
        pvalues = pd.DataFrame(data=sp.concatenate(pv).T,index=data_subsample.geno_ID,columns=["specific","null_common","alternative_any"])
        flag = 0
        qvalues1 = fdr.qvalues(pv[0][0])
        qvalues2 = fdr.qvalues(pv[1][0])
        qvalues3 = fdr.qvalues(pv[2][0])
        for n in range(pvalues.shape[0]):
            k = position.ix[n]['chrom']+':'+str(position.ix[n]['pos'])
            ###ALL.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene])
            if qvalues1[n] < FDR:
                flag = 1
                #print(pvalues)
                #ouFile.write('\t'.join([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]),gene]) + '\n')
                S.append([M[k],position.ix[n]['chrom'],str(position.ix[n]['pos']),str(pvalues.ix[n][0]), str(pvalues.ix[n][1]), str(pvalues.ix[n][2]), str(qvalues1[n]), str(qvalues2[n]), str(qvalues3[n]),gene])
        if flag:
            manhattonPlotSpecific(gene, pvalues,ouF)
    S.sort(cmp = lambda x,y:cmp(float(x[6]),float(y[6])))
    for item in S:
        ouFile.write('\t'.join(item) + '\n')

    ###ALL.sort(cmp = lambda x,y:cmp(float(x[3]),float(y[3])))
    ###for item in ALL:
    ###    ouFile2.write('\t'.join(item) + '\n')
    ###ouFile2.close()
    
    ouFile.close()

#common_effect('Yeast-RNA-ProteinLight-CommonEffect-Sig-Cov')

#any_effect('Yeast-RNA-ProteinLight-AnyEffect-Sig-Cov')
specific_effect('Yeast-RNA-ProteinLight-SpecificEffect-Sig-Cov')

