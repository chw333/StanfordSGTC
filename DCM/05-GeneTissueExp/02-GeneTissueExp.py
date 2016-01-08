### extra output
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pylab as plt


def TissueSample(inF):
    T = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        tissue = fields[1]
        T.setdefault(tissue, [])
        T[tissue].append(sample)
    inFile.close()
    return T
TS = TissueSample('GTEx_Sample2Tissue')

def GeneExp(inF):
    SE = {}
    inFile = open(inF)
    head1 = inFile.readline()
    head2 = inFile.readline()
    head = inFile.readline().strip().split('\t')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene_sym = fields[1]
        gene_id = fields[0]
        SE.setdefault(gene_sym, {})
        SE[gene_sym].setdefault(gene_id, {})
        for i in range(2, len(fields)):
            SE[gene_sym][gene_id][head[i]] = float(fields[i])
    inFile.close()
    return SE
SE = GeneExp('GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.gct')

def TissueExp(gene):
    SE_gene = SE[gene]
    for gene_id in SE_gene:
        TS_EXP = {}
        EXP = SE_gene[gene_id]
        for k in TS:
            TS_EXP.setdefault(k, [])
            for s in TS[k]:
                if s in EXP:
                    TS_EXP[k].append(EXP[s])
        ###
        TE = TS_EXP.items()
        TE.sort(cmp = lambda x,y:cmp(np.median(x[1]), np.median(y[1])), reverse=True)
        EX = []
        SAMPLE = []
        for item in TE:
            EX.append(np.log10(item[1]))
            SAMPLE.append(item[0])
        if 'Heart - Atrial Appendage' in SAMPLE[0:5] or 'Heart - Left Ventricle' in SAMPLE[0:5]:
            print(gene + '\t' + 'Top5')
        else:
            print(gene + '\t' + 'NotTop5')
        fig = plt.figure()
        ax = fig.add_axes([0.25, 0.09, 0.7, 0.85])
        ax.boxplot(EX, vert=False, sym='')

        ax.set_ylim(0,len(SAMPLE)+1)
        ax.set_yticks(range(len(SAMPLE)+2))
        ax.set_yticklabels(['']+SAMPLE+[''], fontsize=6)
        ax.set_xlabel('RPKM (log10)')
        #ax.set_title(gene_id.split('.')[0]+' ('+gene+')')
        ax.set_title(gene)

        #plt.savefig('GTEx_'+gene+'_'+gene_id.split('.')[0]+'.pdf')
        plt.savefig(gene+'.pdf')
        plt.close('all')

def GeneTissueExp(inF): 
    inFile = open(inF)
    ouFile = open(inF+'_NotFound', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split()
        gene = fields[0]
        if gene in SE:
            TissueExp(gene)
        else:
            ouFile.write(gene + '\n')
    inFile.close()
    ouFile.close()

GeneTissueExp('GeneList1')
GeneTissueExp('GeneList2')
GeneTissueExp('GeneList3')


