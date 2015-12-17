def split(inF):
    CH = ['chr'+str(x) for x in range(1, 23)] + ['chrX', 'chrY']
    inFile = open(inF)
    ouFile1 = open(inF.split('.vcf')[0] + '.PASS.vcf', 'w')
    ouFile2 = open(inF.split('.vcf')[0] + '.LowQual.vcf', 'w')
    ouFile3 = open(inF.split('.vcf')[0] + '.OtherChr.vcf', 'w')
    for line in inFile:
        line = line.strip()
        if line[0] == '#':
            ouFile1.write(line + '\n')
            ouFile2.write(line + '\n')
            ouFile3.write(line + '\n')
        else:
            fields = line.split('\t')
            ch = fields[0]
            qual = fields[6]
            if ch in CH:
                if qual == 'PASS':
                    ouFile1.write(line + '\n')
                else:
                    ouFile2.write(line + '\n')
            else:
                ouFile3.write(line + '\n')


    inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

split('Lars_filtered_snp.vcf')
