def filter(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '.filtered', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        name = fields[0]
        D.setdefault(name, [])
        D[name].append(fields)
    inFile.close()
    for k in D:
        if len(D[k]) == 2:
            s1 = int(D[k][0][6])
            e1 = int(D[k][0][7])
            s2 = int(D[k][1][6])
            e2 = int(D[k][1][7])
            if (1<=s1 <=10 and 30<=e1<=70 and 30<=s2<=70 and 90<=e2<=110) or \
                    (1<=s2 <=10 and 30<=e2<=70 and 30<=s1<=70 and 90<=e1<=110):
                        ouFile.write('\t'.join(D[k][0]) + '\n')
                        ouFile.write('\t'.join(D[k][1]) + '\n')
    
    inFile.close()
    ouFile.close()

#filter('SRR1258470-soft-filtered.fa.blated')
filter('SRR1258471-soft-filtered.fa.blated')
