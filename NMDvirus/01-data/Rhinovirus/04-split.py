import os 
Fs = os.listdir('.')

for F in Fs:
    if F[-6:] == '.fastq':
        inFile = open(F)
        ouFile = open(F.split('.fastq')[0] + '.fq', 'w')
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            line3 = inFile.readline().strip()
            line4 = inFile.readline().strip()
            if line1:
                ouFile.write(line1.split()[0] + '#1\n')
                ouFile.write(line2[10:80] + '\n')
                ouFile.write(line3.split()[0] + '#1\n')
                ouFile.write(line4[10:80] + '\n')

                ouFile.write(line1.split()[0] + '#2\n')
                ouFile.write(line2[100:170] + '\n')
                ouFile.write(line3.split()[0] + '#2\n')
                ouFile.write(line4[100:170] + '\n')

            else:
                break
        inFile.close()
        ouFile.close()
