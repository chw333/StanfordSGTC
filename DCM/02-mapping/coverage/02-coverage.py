def coverage(inF):
    MIN = 10
    CH = ['chr' + str(x) for x in range(1, 23)] + ['chrX', 'chrY']
    D = {}
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0] + '.cov'+str(MIN), 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[0]
        pos = int(fields[1])
        num = int(fields[2])
        ### covered sites, cumulated reads number, total sites
        D.setdefault(ch, [0, 0, 0])
        D[ch][2] += 1
        if num > MIN:
            D[ch][0] += 1
            D[ch][1] += num
    inFile.close()
    
    T0 = 0
    T1 = 0
    T2 = 0
    for ch in CH:
        try:
            ouFile.write('\t'.join([ch, str(D[ch][2]), str(D[ch][0]), str(D[ch][1]), '%.1f'%(D[ch][1]/D[ch][2]), '%.1f'%(D[ch][1]/D[ch][0])]) + '\n')
            T0 += D[ch][0]
            T1 += D[ch][1]
            T2 += D[ch][2]
        except:
            pass
    try:
        ouFile.write('\t'.join(['Total', str(T2), str(T0), str(T1), '%.1f'%(T1/T2), '%.1f'%(T1/T0)]) + '\n')
    except:
        pass
    ouFile.close()
coverage('Lars_coverage.txt')
