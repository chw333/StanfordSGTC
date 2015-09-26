D = {}
def ref(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        if line[0] != '#':
            fields = line.split('\t')
            k = '\t'.join([fields[0], fields[1], fields[3], fields[4]])
            D.setdefault(k, 0)
            D[k] += 1
    inFile.close()

ref('YJM789a.flt.vcf')
ref('YJM789b.flt.vcf')

def replace(inF):
    GN = {}
    CH = []
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            GN[line1[1:]] = list(line2)
            CH.append(line1[1:])
        else:
            break
    inFile.close()
    for k in D:
        fields = k.split('\t')
        pos = int(fields[1]) - 1
        ch = fields[0]
        rf = fields[2]
        alt = fields[3]
        if GN[ch][pos] == rf:
            #if len(alt) == 1:
            GN[ch][pos] = 'N'

    ouFile = open(inF.split('.fsa.fa')[0] + '.YJM789.fa', 'w')
    for ch in CH:
        ouFile.write('>' + ch + '\n')
        ouFile.write(''.join(GN[ch]) + '\n')
    ouFile.close()

replace('S288C_reference_sequence_R64-2-1_20150113.fsa.fa')


        
