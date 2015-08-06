import numpy
D = {}
inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Filtered-Median')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[2:]:
        snp = item.split(':')[0]
        exp = float(item.split('#')[-1])
        D.setdefault(snp, [])
        D[snp].append(exp)
inFile.close()


G = {}
for k in D:
    m = sorted(D[k])
    G[k] = numpy.median(m)
    #print(D[k])
    #print(G[k])

inFile = open('G462-Sample-Stopgain-Exon-Escape')
ouFile = open('G462-Sample-Stopgain-Exon-Escape-Exp', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    snp = fields[0]
    if snp in G:
        ouFile.write(line + '\t' + str(G[snp]) + '\n')
    else:
        pass
        
inFile.close()
ouFile.close()

