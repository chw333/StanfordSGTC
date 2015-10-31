L = []
inFile = open('AnnotatedFeatures.gff')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
inFile.close()

def intersect(inF):
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        region = fields[0].split('_')
        ch = 'chr' + region[0]
        start = int(region[1])
        end = int(region[2])
    inFile.close()

intersect('MHCII_high_Tspan8_PositiveNegative_sig.txt')
