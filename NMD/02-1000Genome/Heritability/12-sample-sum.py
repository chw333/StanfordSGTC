import numpy
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sample', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        s1 = 0
        s2 = 0
        L = []
        for item in fields[1:]:
            esc = item.split(':')[-1]
            if esc == 'unEscaped':
                v1 = int(item.split('&')[1].split(':')[0])
                v2 = int(item.split('&')[1].split(':')[1])
                s1 += v1
                s2 += v2
                L.append((v2+1.0)/(v1+1.0))
        #ouFile.write(sample + '\t' + str(s1) +'\t' +str(s2)+ '\t' + str((s2+1.0)/(s1+1.0)) + '\n')
        if L:
            ouFile.write(sample + '\t' + str((s2+1.0)/(s1+1.0)) + '\t' + str(numpy.std(L)) + '\n')

    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Sum-Escape')
