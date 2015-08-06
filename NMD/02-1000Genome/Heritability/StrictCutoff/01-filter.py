MIN = 2
def filter(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Filtered', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        LS = [sample]
        for item in fields[2:]:
            ims = item.split('#')
            snp = ims[0]
            exp = ims[1].split('_')
            L = []
            flag = 1
            for ep in exp:
                v1 = int(ep.split('%')[0])
                v2 = int(ep.split('%')[1])
                if v1 == -1 or v2 == -1:
                    flag = 0
                    pass
                elif v1 == 0 or v2 ==0:
                    flag = 0
                else:
                    if v1 >= v2:
                        L.append(1)
                    else:
                        L.append(0)
            if flag:
                if 1 not in L or 0 not in L:
                    if len(L) >= MIN:
                        LS.append(item)
        if len(LS) > 1:
            ouFile.write('\t'.join(LS) + '\n')
    ouFile.close()
            



filter('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
