inFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered')
ouFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered-Ratio', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[2:]:
        fds = item.split(':')
        esc = item[0]
        rat = (float(fds[-1]) + 1) / (float(fds[-2]) + 1)
        snp = fds[1]
        ouFile.write(snp + '\t' + esc + '\t' + str(rat) + '\n')
inFile.close()
ouFile.close()


inFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered2')
ouFile = open('G462-Sample-Stopgain-ASE-Escape-Filtered2-Ratio', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[2:]:
        fds = item.split(':')
        esc = item[0]
        rat = (float(fds[-1]) + 1) / (float(fds[-2]) + 1)
        snp = fds[1]
        ouFile.write(snp + '\t' + esc + '\t' + str(rat) + '\n')
inFile.close()
ouFile.close()
