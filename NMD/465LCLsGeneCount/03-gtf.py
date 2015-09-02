inFile = open('Homo_sapiens.GRCh37.75.gtf')
ouFile = open('Homo_sapiens.GRCh37.75.chr.gtf', 'w')
CHR = [str(x) for x in range(1,23)] + ['X', 'Y']
for line in inFile:
    line = line.strip()
    if line[0] == '#':
        ouFile.write(line + '\n')
    else:
        fields= line.split('\t')
        ch = fields[0]
        if ch in CHR:
            ouFile.write('chr' + line + '\n')

inFile.close()
ouFile.close()
