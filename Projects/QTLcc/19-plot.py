import pylab as pl
def plot(inF, xc, title):
    CH = {}
    CH['chr01'] = 0
    CH['chr02'] = 0
    CH['chr03'] = 0
    CH['chr04'] = 0
    CH['chr05'] = 0
    CH['chr06'] = 0
    CH['chr07'] = 0
    CH['chr08'] = 0
    CH['chr09'] = 0
    CH['chr10'] = 0
    CH['chr11'] = 0
    CH['chr12'] = 0
    CH['chr13'] = 0
    CH['chr14'] = 0
    CH['chr15'] = 0
    CH['chr16'] = 0
    L = []
    inFile =  open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[3]
        if ch in ['1']:
            CH['chr01'] += 1
        if ch in ['1','2']:
            CH['chr02'] += 1
        if ch in ['1','2','3']:
            CH['chr03'] += 1
        if ch in [str(x) for x in range(1,5)]:
            CH['chr04'] += 1
        if ch in [str(x) for x in range(1,6)]:
            CH['chr05'] += 1
        if ch in [str(x) for x in range(1,7)]:
            CH['chr06'] += 1
        if ch in [str(x) for x in range(1,8)]:
            CH['chr07'] += 1
        if ch in [str(x) for x in range(1,9)]:
            CH['chr08'] += 1
        if ch in [str(x) for x in range(1,10)]:
            CH['chr09'] += 1
        if ch in [str(x) for x in range(1,11)]:
            CH['chr10'] += 1
        if ch in [str(x) for x in range(1,12)]:
            CH['chr11'] += 1
        if ch in [str(x) for x in range(1,13)]:
            CH['chr12'] += 1
        if ch in [str(x) for x in range(1,14)]:
            CH['chr13'] += 1
        if ch in [str(x) for x in range(1,15)]:
            CH['chr14'] += 1
        if ch in [str(x) for x in range(1,16)]:
            CH['chr15'] += 1
        if ch in [str(x) for x in range(1,17)]:
            CH['chr16'] += 1

        L.append(int(fields[-1]))
    inFile.close()

    fig = pl.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(len(L)), L, color = xc)
    M = []
    M.append(0 + (CH['chr01'])/2)
    M.append(CH['chr01'] + (CH['chr02'])/2)
    M.append(CH['chr02'] + (CH['chr03'])/2)
    M.append(CH['chr03'] + (CH['chr04'])/2)
    M.append(CH['chr04'] + (CH['chr05'])/2)
    M.append(CH['chr05'] + (CH['chr06'])/2)
    M.append(CH['chr06'] + (CH['chr07'])/2)
    M.append(CH['chr07'] + (CH['chr08'])/2)
    M.append(CH['chr08'] + (CH['chr09'])/2)
    M.append(CH['chr09'] + (CH['chr10'])/2)
    M.append(CH['chr10'] + (CH['chr11'])/2)
    M.append(CH['chr11'] + (CH['chr12'])/2)
    M.append(CH['chr12'] + (CH['chr13'])/2)
    M.append(CH['chr13'] + (CH['chr14'])/2)
    M.append(CH['chr14'] + (CH['chr15'])/2)
    M.append(CH['chr15'] + (CH['chr16'])/2)
    ax.set_xlim(0, CH['chr16'])
    ax.set_xticks(M)
    ax.set_ylabel('Number of QTLs')
    ax.set_xticklabels(['chr'+str(x) for x in range(1,17)],rotation='vertical')
    ax.set_title(title)
    pl.savefig(inF + '.pdf')



plot('Yeast-RNA-ProteinLight-CommonEffect-Sig-noCov-Merged-chr', 'r', 'Common Effect')

plot('Yeast-Single-Trait-Merged-ProteinLightSpecific-chr', 'b', 'Protein Specific Effect')
