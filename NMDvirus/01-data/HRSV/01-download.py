inFile = open('SRP010162.txt')
ouFile = open('01-download.sh', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ftp = fields[-2].split(';')
    for x in ftp:
        ouFile.write('wget ' + x + '\n')

inFile.close()
ouFile.close()
