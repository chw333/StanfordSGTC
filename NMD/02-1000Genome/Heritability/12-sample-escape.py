D = {}
inFile = open('G462-Sample-Stopgain-Exon-Escape')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[-1]
inFile.close()

inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Sum')
ouFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Sum-Escape', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    LS = [fields[0]]
    for fd in fields[1:]:
        snp = fd.split(':')[0]
        if D[snp] == 'T':
            LS.append(fd + ':Escaped')
        else:
            LS.append(fd + ':unEscaped')
    ouFile.write('\t'.join(LS) + '\n')
inFile.close()
ouFile.close()
