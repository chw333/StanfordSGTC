D = {}
inFile = open('GD462.ASE.COV8.ANNOT_PTV.txt')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0].split('.')[0]
    snp = fields[1]
    ref = fields[6]
    alt = fields[7]
    k = sample + '\t' + snp
    D[k] = ':'.join([ref, alt])
inFile.close()

def exp(inF):
    S = {}
    inFile = open(inF)
    ouFile = open(inF + '-Exp', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        num = fields[1]
        LS = [sample, num]
        for item in fields[2:]:
            ims = item.split('+')
            L = []
            #im = ims[0]
            #snp = im.split(':')[0]
            #k = sample + '\t' + snp
            #if k in D:
            #    L.append(im + ':' + D[k])
            #else:
            #    L.append(im + ':-1:-1')
            for im in ims:
                snp = im.split(':')[0]
                k = sample + '\t' + snp
                if k in D:
                    L.append(im + ':' + D[k])
                else:
                    L.append(im + ':-1:-1')
            LS.append('+'.join(L))
        ouFile.write('\t'.join(LS) + '\n')

    inFile.close()
    ouFile.close()

exp('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype')
