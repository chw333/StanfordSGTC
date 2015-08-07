import numpy
def median(inF):
    inFile = open(inF)
    ouFile = open(inF + '-Sum', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        num = fields[1]
        S = [sample]
        for item in fields[2:]:
            im = item.split('+')
            #snp = im[0]
            s0 = 0
            s1 = 0
            #exp = im[1].split('_')
            for imx in im:
                snp = imx.split('#')[0]
                exp = imx.split('#')[1]
                two = exp.split(':')
                if two[0] == '-1' or two[1] == '-1':
                    pass
                elif two[0] == '0' or two[1] == '0':
                    pass
                elif int(two[0]) + int(two[1]) > 30:
                    s0 += int(two[0])
                    s1 += int(two[1])
            if s0 > 0 or s1 > 0:
                S.append(item + '&' + str(s0) + ':' + str(s1))
        ouFile.write('\t'.join(S) + '\n')




    inFile.close()
    ouFile.close()

median('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
