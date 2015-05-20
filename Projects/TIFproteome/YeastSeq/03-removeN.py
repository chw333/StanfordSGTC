import sys
inF = sys.argv[1]
if inF[-6:] == '.fastq':
    inFile = open(inF)
    ouFile = open(inF[0:-6] + '.noN.fastq', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        line3 = inFile.readline().strip()
        line4 = inFile.readline().strip()
        if line1:
            flag = 0
            for x in line2:
                if x not in ['A','T','C','G']:
                    flag = 1
            if not flag:
                ouFile.write(line1 + '\n')
                ouFile.write(line2 + '\n')
                ouFile.write(line3 + '\n')
                ouFile.write(line4 + '\n')
        else:
            break
    inFile.close()
    ouFile.close()
