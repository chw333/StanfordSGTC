inFile = open('RSV-Stopgain-SNV')
ouFile1 = open('RSV-Stopgain-SNV-het', 'w')
ouFile2 = open('RSV-Stopgain-SNV-hom', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[9] == 'het':
        ouFile1.write(line + '\n')
    elif fields[9] == 'hom':
        ouFile2.write(line + '\n')
    else:
        print(line)
inFile.close()
ouFile1.close()
ouFile2.close()
