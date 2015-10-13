G = []
inFile = open('/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/StopGain/RSV2-Stopgain-SNV-het-gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if int(fields[1]) >= 2:
        G.append(fields[0])
inFile.close()

ouFile = open('RSV2-Stopgain-SNV-ReadCount-Filtered', 'w')
for g in G:
    inFile = open('RSV2-Stopgain-SNV-ReadCount')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == g:
            ouFile.write(line + '\n')
    inFile.close()
ouFile.close()
