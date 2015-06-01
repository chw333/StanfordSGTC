MU = ['stopgain', 'stoploss', 'frameshift substitution']
CH = ['chr' + str(x) for x in range(1,23)]
def classify():
    ouFile1 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-StopGainLossFrameshift', 'w')
    ouFile2 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stopgain', 'w')
    ouFile3 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-stoploss', 'w')
    ouFile4 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-frameshift', 'w')
    ouFile5 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-mis', 'w')
    ouFile6 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-synonymous', 'w')
    ouFile7 = open('GEUVADIS.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype-nonSynonymous', 'w')
    D = {}
    for ch in CH:
        inFile = open('GEUVADIS.' + ch + '.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes-Genotype.exonic_variant_function')
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if '1' not in fields[11:] and '2' not in fields[11:]:
                ouFile5.write(line + '\n')
            else:
                mutation_type = fields[1]
                D[mutation_type] = 1
                if mutation_type in MU:
                    ouFile1.write(line + '\n')
                    if mutation_type == 'stopgain':
                        ouFile2.write(line + '\n')
                    if mutation_type == 'stoploss':
                        ouFile3.write(line + '\n')
                    if mutation_type == 'frameshift substitution':
                        ouFile4.write(line + '\n')
                elif mutation_type == 'synonymous SNV':
                        ouFile6.write(line + '\n')
                elif mutation_type == 'nonsynonymous SNV':
                        ouFile7.write(line + '\n')
        inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()
    ouFile4.close()
    ouFile5.close()
    ouFile6.close()
    ouFile7.close()
    for k in D:
        print(k)

classify()

