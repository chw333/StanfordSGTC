import glob
Fs = glob.glob('*.flt.vcf')
for F in Fs:
    inFile = open(F)
    ouFile = open(F[0:-4] + '.bias', 'w')
    for line in inFile:
        line = line.strip()
        if line[0:2] != '##':
            fields = line.split('\t')
            info = fields[7]
            if info.find('DP4') != -1:
                k = '_'.join([fields[0], fields[1], fields[3], fields[4]])
                DP4= info.split('DP4=')[1].split(';')[0].split(',')
                DP4ref = int(DP4[0]) + int(DP4[1])
                DP4alt = int(DP4[2]) + int(DP4[3])
                ouFile.write(k + '\t' + str(DP4ref) + '\t' + str(DP4alt) + '\n')
            else:
                print(line)
    inFile.close()
    ouFile.close()
