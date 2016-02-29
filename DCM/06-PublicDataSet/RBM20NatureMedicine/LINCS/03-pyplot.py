import matplotlib
matplotlib.use('Agg')
import pylab as pl
from pylab import cm
#colors = [('white')] + [(color(i)) for i in xrange(1,256)]

TOP = 20
def plot(inF, color='red', title=None):


    if not title:
        title = '_'.join(inF.split('_')[-2:])

    inFile = open(inF)
    TFX = []
    LX = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        LX.append([abs(float(x)) for x in fields[1:]])
        TFX.append(fields[0])
    inFile.close()

    L = LX[0:TOP]
    TF = TFX[0:TOP]

    if L:
        print(title)
        colors = ['white',color]
        new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
        fig = pl.figure()
        ax = fig.add_axes([0.1,0.05,0.8,0.8])

        ax.matshow(L, cmap=new_map)
        ax.set_xticks(range(len(L[0])))
        ax.set_xticklabels([])
        ax.set_yticklabels(TF)
        ax.set_yticks(range(len(L)))
        #ax.set_xticklabels(Gene, rotation='vertical')
        ax.set_title(title)
        pl.grid()
        pl.savefig(inF + '.pdf')

plot('result_UPTAG_summly_n7503_drug_anti-connection',color='green')
plot('result_UPTAG_summly_n7503_drug_connection', color='red')
plot('result_UPTAG_summly_n7503_geneKnockdown_anti-connection',color='green')
plot('result_UPTAG_summly_n7503_geneKnockdown_connection',color='red')
plot('result_UPTAG_summly_n7503_geneOverexpress_anti-connection',color='green')
plot('result_UPTAG_summly_n7503_geneOverexpress_connection',color='red')


