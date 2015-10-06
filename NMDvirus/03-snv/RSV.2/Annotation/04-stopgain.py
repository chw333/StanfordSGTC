Sample = ['HRSV0h-rep1.flt.anno.exonic_variant_function','HRSV0h-rep2.flt.anno.exonic_variant_function','HRSV2h-rep1.flt.anno.exonic_variant_function','HRSV2h-rep2.flt.anno.exonic_variant_function','HRSV4h-rep1.flt.anno.exonic_variant_function','HRSV4h-rep2.flt.anno.exonic_variant_function','HRSV8h-rep1.flt.anno.exonic_variant_function','HRSV8h-rep2.flt.anno.exonic_variant_function','HRSV12h-rep1.flt.anno.exonic_variant_function','HRSV12h-rep2.flt.anno.exonic_variant_function','HRSV16h-rep1.flt.anno.exonic_variant_function','HRSV16h-rep2.flt.anno.exonic_variant_function','HRSV20h-rep1.flt.anno.exonic_variant_function','HRSV20h-rep2.flt.anno.exonic_variant_function','HRSV24h-rep1.flt.anno.exonic_variant_function','HRSV24h-rep2.flt.anno.exonic_variant_function']

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

ouFile = open('RSV-Stopgain', 'w')
for item in L:
    ouFile.write('\t'.join(item) + '\n')
ouFile.close()

