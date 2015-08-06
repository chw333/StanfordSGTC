def dep(sample, snp):
    return [20,10]

inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')
ouFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Exp', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    num = fields[1]
    LS = [sample, num]
    for item in fields[2:]:
        L = []
        fds = item.split('|')
        for fd in fds:
            snp = fd.split(':')[0]
            ch = snp.split('_')[1]
            pos = snp.split('_')[2]
            dp = dep(sample,snp)
            L.append(fd + ':' + ':'.join([str(x) for x in dp]))
        LS.append('|'.join(L))
    ouFile.write('\t'.join(LS) + '\n')

inFile.close()
ouFile.close()


