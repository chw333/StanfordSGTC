def count(inF, inF2, ouF):
    D = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        D.setdefault(k, {})
        D[k]['info'] = fields
        for item in fields[5:]:
            fds = item.split(':')
            D[k][fds[0]] = int(fds[1])
    inFile.close()

    inFile = open(inF2)
    ouFile = open(ouF, 'w')
    for line in inFile:
        line = line.strip()
        if line[0] != '#':
            fields = line.split('\t')
            info = fields[7]
            DP4 = info.split('DP4=')[1].split(';')[0].split(',')
            ch = fields[0]
            pos = fields[1]
            ref = fields[3]
            alt = fields[4]
            ref_count = int(DP4[0]) + int(DP4[1])
            alt_count = int(DP4[2]) + int(DP4[3])
            k = ch + '\t' + pos
            if k in D:
                '''
                if ref == 'A' and alt == 'T':
                    ref_count2 = D[k]['A']
                    alt_count2 = D[k]['T']
                elif ref == 'A' and alt == 'C':
                    ref_count2 = D[k]['A'] + D[k]['T']
                    alt_count2 = D[k]['C'] + D[k]['G']
                elif ref == 'A' and alt == 'G':
                    ref_count2 = D[k]['A'] + D[k]['T']
                    alt_count2 = D[k]['C'] + D[k]['G']
                elif ref == 'T' and alt == 'A':
                    ref_count2 = D[k]['T']
                    alt_count2 = D[k]['A']
                elif ref == 'T' and alt == 'C':
                    ref_count2 = D[k]['A'] + D[k]['T']
                    alt_count2 = D[k]['C'] + D[k]['G']
                elif ref == 'T' and alt == 'G':
                    ref_count2 = D[k]['A'] + D[k]['T']
                    alt_count2 = D[k]['C'] + D[k]['G']
                elif ref == 'C' and alt == 'A':
                    ref_count2 = D[k]['C'] + D[k]['G']
                    alt_count2 = D[k]['A'] + D[k]['T']
                elif ref == 'C' and alt == 'T':
                    ref_count2 = D[k]['C'] + D[k]['G']
                    alt_count2 = D[k]['A'] + D[k]['T']
                elif ref == 'C' and alt == 'G':
                    ref_count2 = D[k]['C']
                    alt_count2 = D[k]['G']
                elif ref == 'G' and alt == 'A':
                    ref_count2 = D[k]['C'] + D[k]['G']
                    alt_count2 = D[k]['A'] + D[k]['T']
                elif ref == 'G' and alt == 'T':
                    ref_count2 = D[k]['C'] + D[k]['G']
                    alt_count2 = D[k]['A'] + D[k]['T']
                elif ref == 'G' and alt == 'C':
                    ref_count2 = D[k]['G']
                    alt_count2 = D[k]['C']
                '''
                if D[k]['info'][2] == 'N':
                    if ref in ['A','T','C','G'] and alt in ['A','T','C','G']:
                        ref_count2 = D[k][ref]
                        alt_count2 = D[k][alt]
                        ouFile.write('\t'.join([ch, pos, ref, alt, str(ref_count), str(alt_count), str(ref_count2), str(alt_count2)]) + '\n')

    inFile.close()
    ouFile.close()

count('5a-MaskN-Count', '../5a.flt.vcf', '5a-Allele-Count')
count('5b-MaskN-Count', '../5b.flt.vcf', '5b-Allele-Count')
