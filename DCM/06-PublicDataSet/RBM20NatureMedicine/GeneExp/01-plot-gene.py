import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot(gene):
    df = pd.read_table(gene,  header=-1)
    df=pd.DataFrame(df.ix[0,2:5])
    df.index=['S635A','CP1','CP2']
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df.plot(kind='bar', rot=1, ax = ax, legend=False)
    ax.set_title(gene)
    ax.set_ylabel('Normalized gene expression')
    plt.savefig(gene + '.pdf')

plot('RBM20')
plot('EGR1')
