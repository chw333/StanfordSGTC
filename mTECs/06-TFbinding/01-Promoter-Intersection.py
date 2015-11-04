L = []
inFile = open('AnnotatedFeatures.gff')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

def intersect(inF):
    inFile = open(inF)
    ouFile = open(inF.split('.txt')[0] + '.Feature', 'w')
    head = inFile.readline()
    for line in inFile:
        S = set()
        line = line.strip()
        fields = line.split('\t')
        region = fields[0].split('_')
        ch = 'chr' + region[1]
        start = int(region[2])
        end = int(region[3])
        for item in L:
            if item[0] == ch:
                if int(item[4]) < start or int(item[3]) > end:
                    pass
                else:
                    S.add('|'.join(item))
        ouFile.write(line + '\t' + '\t'.join(S) + '\n')


    inFile.close()
    ouFile.close()

intersect('MHCII_high_Tspan8_PositiveNegative_sig.txt')
intersect('Tspan8_positive_MHCII_HighLow_sig.txt')
intersect('MHCII_low_Tspan8_PositiveNegative_sig.txt')
intersect('Tspan8_negative_MHCII_HighLow_sig.txt')
