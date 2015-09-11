import matplotlib
matplotlib.use('Agg')
import pandas as pd
import pylab as pl
import matplotlib.patches as patches


def readData(inF):
    D = {}
    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    Gene = head[1:]
    Virus = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        virus = fields[0]
        Virus.append(virus)
        D.setdefault(virus, {})
        for i in range(1, len(head)):
            D[virus][head[i]] = fields[i]
    inFile.close()
    return([D, Virus, Gene])
data = readData('NMD-Substrate-Exp')


def myPlot():
    Gene = data[2]
    Virus = data[1][::-1]
    D = data[0]

    N_Panel = 6
    N_Gene = 14
    
    fig = pl.figure()
    AX = []
    for i in range(N_Panel):
        ax = fig.add_axes([0.08, 0.12+0.14*i, 0.82, 0.14])
        ax.set_xlim(0,N_Gene + 1)
        ax.set_xticks(range(N_Gene + 2))
        ax.get_xaxis().set_visible(False)
        ax.set_xticklabels([])
        #ax.set_yticklabels([])
        AX.append(ax)

    AX[0].set_xticklabels(['']+Gene+[''],rotation=45,fontsize=10)
    AX[0].xaxis.set_ticks_position('bottom')
    AX[0].get_xaxis().set_visible(True)

    
    for x in range(N_Panel):
        V = []
        for i in range(len(Gene)):
            val = D[Virus[x]][Gene[i]].split(':')
            if val[1] != 'NA':
                if float(val[0]) > 20:
                    V.append(float(val[1]))
        AX[x].set_ylim(min(V)-1, max(V) + 1)
        AX[x].set_yticks(range(int(min(V)), int(max(V)+1.5),2))
        c = (min(V) + max(V)) / 2
        vs = Virus[x]
        if Virus[x] == 'HIV1':
            vs = 'HIV-1'
        elif Virus[x] == 'HSV1':
            vs = 'HSV-1'
        AX[x].text(N_Gene + 1.2,c, vs, va='center',ha='left')



    for i in range(1, N_Gene + 1):
        x = i - 0.3
        width = 0.6
        for p in range(N_Panel):
            y = AX[p].get_ylim()[0]
            height = AX[p].get_ylim()[1] - AX[p].get_ylim()[0]
            AX[p].add_patch(patches.Rectangle((x,y),width,height,fill=True, linewidth=0, facecolor='lightgray',alpha=0.7))

    for x in range(0,N_Panel):
        for i in range(len(Gene)):
            val = D[Virus[x]][Gene[i]].split(':')
            if val[1] != 'NA':
                if float(val[0]) > 20:
                    if float(val[2]) < 0.05:
                        AX[x].scatter(i+1, float(val[1]),color='red',alpha=1,zorder=10)
                    else:
                        AX[x].scatter(i+1, float(val[1]),color='black',alpha=1,zorder=10)
        AX[x].plot([0,N_Gene+1],[0,0], linestyle='--')

    

    fig.text(0.02, 0.5, 'log2 fold change (virus/mock)', rotation='vertical', va='center')

    pl.savefig('NMD-Virus.pdf')

myPlot()


