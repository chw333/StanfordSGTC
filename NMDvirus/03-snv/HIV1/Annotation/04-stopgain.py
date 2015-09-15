Sample = ['Mock_12-rep1.flt.anno.exonic_variant_function','Mock_12-rep2.flt.anno.exonic_variant_function','Mock_12-rep3.flt.anno.exonic_variant_function','Mock_24-rep1.flt.anno.exonic_variant_function','Mock_24-rep2.flt.anno.exonic_variant_function','HIV_12-rep1.flt.anno.exonic_variant_function','HIV_12-rep2.flt.anno.exonic_variant_function','HIV_12-rep3.flt.anno.exonic_variant_function','HIV_24-rep1.flt.anno.exonic_variant_function','HIV_24-rep2.flt.anno.exonic_variant_function','HIV_24-rep3.flt.anno.exonic_variant_function']

L = []
for s in Sample:
    sa = s.split('.')[0]
    inFile = open(s)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[2].split(':')[0]
        if fields[1] == 'stopgain':
            L.append([sa, gene] + fields[1:])
    inFile.close()

ouFile = open('HIV-Stopgain', 'w')
for item in L:
    ouFile.write('\t'.join(item) + '\n')
ouFile.close()

