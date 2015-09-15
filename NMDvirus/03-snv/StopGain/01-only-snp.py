def stopgain(inF):
    inFile = open(inF)
    ouFile = open(inF + '-SNV', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields[7]) == 1 and len(fields[8]) == 1:
            if fields[7] in ['A','T','C','G'] and fields[8] in ['A','T','C','G']:
                ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

stopgain('HCV-Stopgain')
stopgain('HIV-Stopgain')
stopgain('HSV-Stopgain')
stopgain('KHSV-Stopgain')
stopgain('RSV-Stopgain')
stopgain('WNV-Stopgain')
