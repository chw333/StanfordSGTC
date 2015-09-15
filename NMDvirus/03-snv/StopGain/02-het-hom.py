def hethom(inF):
    inFile = open(inF)
    ouFile1 = open(inF + '-het', 'w')
    ouFile2 = open(inF + '-hom', 'w')
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

hethom('HCV-Stopgain-SNV')
hethom('HIV-Stopgain-SNV')
hethom('HSV-Stopgain-SNV')
hethom('KHSV-Stopgain-SNV')
hethom('RSV-Stopgain-SNV')
hethom('WNV-Stopgain-SNV')
