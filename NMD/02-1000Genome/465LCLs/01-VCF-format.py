def format(inF):
    ouFile = open(inF.split('.vcf')[0] + '-Genotype', 'w')
    ouFile2 = open(inF.split('.vcf')[0] + '-Head', 'w')

    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if line[0] == '#':
            if line.find('#CHROM') == 0:
                sample = fields[9:]
        else:
            ch = fields[0]
            start = fields[1]
            ID = fields[2]
            ref = fields[3]
            alt = fields[4]
            QUAL = fields[5]
            FILTER = fields[6]
            end = str(int(start) + len(ref) - 1)
            if ref.find(',') != -1 or ref.find(';') !=-1 or alt.find(',') != -1 or alt.find(';') !=-1:
                print(line)
            L = []
            for item in fields[9:]:
                g = ''
                its = item.split(':')
                if its[0] == '.':
                    g = '-1'
                elif its[0] == '0|0' or its[0] == '0/0':
                    g = '0'
                elif its[0] == '0|1' or its[0] == '0/1' or its[0] == '1|0' or its[0] == '1/0':
                    g = '1'
                elif its[0] == '1|1' or its[0] == '1/1':
                    g = '2'
                else:
                    print(item)
                L.append(g)
            ouFile.write('\t'.join([ch, start, end, ref, alt] + [ID, QUAL, FILTER ] + L) + '\n')
    inFile.close()
    ouFile2.write('\t'.join(['CHROME', 'START', 'END', 'REF', 'ALT', 'ID', 'QUAL', 'FILTER'] + sample) + '\n')
    ouFile.close()
    ouFile2.close()


#format('GEUVADIS.chr22.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr10.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr11.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr12.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr13.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr14.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr15.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr16.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr17.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr18.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr19.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr1.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr20.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr21.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr22.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr2.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr3.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr4.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr5.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr6.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr7.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr8.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
format('GEUVADIS.chr9.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf')
