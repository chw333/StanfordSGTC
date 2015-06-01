def Sort(inF):
    D = {}
    ouFile = open(inF + '-sorted', 'w')
    inFile = open(inF)
    head = inFile.readline()
    ouFile.write(head)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[0]
        D.setdefault(gene, [])
        D[gene].append(line)
    inFile.close()

    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse=True)
    for item in d:
        ouFile.write('\n'.join(item[1]) + '\n')
    ouFile.close()


#Sort('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain-formated')
Sort('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-synonymous-formated')
Sort('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-nonSynonymous-formated')
